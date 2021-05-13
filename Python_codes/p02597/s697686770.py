N = int(input())
S = input()
w = 0
r = 0
for s in S:
    if s == "W":
        w += 1
    else:
        r += 1

res = r
rcnt = [0 for i in range(N+1)]
wcnt = [0 for i in range(N+1)]

for i in range(N):
    if S[i] == "W":
        wcnt[i+1] = wcnt[i] + 1
        rcnt[i+1] = r
    else:
        r -= 1
        rcnt[i+1] = r
        wcnt[i+1] = wcnt[i]
    res = min(res, max(wcnt[i+1], rcnt[i+1]))
print(res)