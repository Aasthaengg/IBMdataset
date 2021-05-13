n = int(input())
ab=[]
for i in range(n):
    a,b = map(int,input().split())
    ab.append([a,b])
ans = 0
for i in range(n-1,-1,-1):
        c = (ab[i][0]+ans)%ab[i][1]
        if c!=0:
            ans += ab[i][1]-c
print(ans)
