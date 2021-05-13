N = int(input())
S = list(input())

count = []
for i in range(N):
    count.append([0,0])

cb = 0
for i in range(N):
    count[i][0] = cb
    if S[i] == "#":
        cb += 1
cw = 0
for i in range(N):
    count[N-i-1][1] = cw
    if S[N-i-1] == ".":
        cw += 1

ans = 10**10
for i in range(N):
    ans = min(ans,sum(count[i]))
print(ans)