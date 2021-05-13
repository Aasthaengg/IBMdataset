N = int(input())
s = list(input())

l, r = [[0]*2 for _ in range(N+1)], [[0]*2 for _ in range(N+1)]
for i,j in enumerate(s, start=1):
    if j=="#":
        l[i][1] = l[i-1][1]
        l[i][0] = l[i-1][0] + 1
    else:
        l[i][0] = l[i-1][0]
        l[i][1] = l[i-1][1] + 1

for i,j in enumerate(s[::-1], start=1):
    if j=="#":
        r[N-i][1] = r[N-i+1][1]
        r[N-i][0] = r[N-i+1][0] + 1
    else:
        r[N-i][0] = r[N-i+1][0]
        r[N-i][1] = r[N-i+1][1] + 1

ans = N
for i in range(N+1):
    ans = min(ans, l[i][0]+r[i][1])

print(ans)