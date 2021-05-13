N=int(input())
F = []
for _ in range(N):
    s = input().split()
    F.append(int("".join(s), base=2))
P = [list(map(int, input().split())) for _ in range(N)]
ans = -float("inf")
for bit in range(1, 2**10):
    gain = 0
    for i in range(N):
        ci = 0
        for j in range(10):
            if ((bit>>j) & 1) and ((F[i]>>j) & 1):
                ci += 1
        gain += P[i][ci]
    ans = max(ans, gain)
print(ans)