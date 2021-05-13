h, w, k = map(int, input().split())
S = [list(input()) for _ in range(h)]
ans = []
n = 1
cnt = 0
for i in range(h):
    if "#" in S[i]:
        ans = []
        for j in range(w):
            if S[i][j] == "#":
                for _ in range(j+1-len(ans)):
                    ans.append(str(n))
                n += 1
        if len(ans) < w:
            x = ans[-1]
            for _ in range(w-len(ans)):
                ans.append(x)
    if ans:
        for _ in range(i+1-cnt):
            print(" ".join(ans))
            cnt += 1

