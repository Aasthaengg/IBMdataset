n,m = map(int,input().split())
s,c = [],[]
for i in range(n):
    a = list(map(int,input().split()))
    s.append(a)
for i in range(m):
    a = list(map(int,input().split()))
    c.append(a)


for i in range(n):
    tmp = 10**16
    ans = 0
    for j in range(m):
        b = (abs(s[i][0]-c[j][0])+abs(s[i][1]-c[j][1]))
        if tmp > b:
            tmp = b
            ans = j+1
    print(ans)