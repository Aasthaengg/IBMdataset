n,c = map(int,input().split())
l = [[0]*(10**5+5) for _ in range(c)]
for i in range(n):
    s,t,k = map(int,input().split())
    l[k-1][s-1] += 1
    l[k-1][t-1] -= 1
for i in range(c):
    for j in range(1,10**5+2):
        l[i][j] += l[i][j-1]

for i in range(c):
    for j in range(10**5+2):
        if l[i][j] == 0 and l[i][j+1] == 1:
            l[i][j] = 1
ans = 0
for j in range(10**5+1):
    s = 0
    for i in range(c):
        s += l[i][j]
    ans = max(ans,s)

print(ans)