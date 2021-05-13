import sys
input = sys.stdin.readline
H, W, K = map(int, input().split())
S = [input()[:-1] for _ in [0]*H]
N = H+W
ans = 0
for bitH in range(1 << H):
    T = []
    for h in range(H):
        if bitH >> h & 1:
            T.append(S[h])

    for bitW in range(1 << W):
        cnt = 0
        for w in range(W):
            if bitW >> w & 1:
                for t in T:
                    cnt += 1 if t[w] == "#" else 0

        if cnt == K:
            ans += 1

print(ans)
