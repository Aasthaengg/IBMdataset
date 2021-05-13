n,x = map(int,input().split())
l = list(map(int,input().split()))
d = [0]*(n+1)
ans = 1

for i in range(1,n+1):
    d[i] = d[i-1]+l[i-1]
    if x < d[i]:
        break
    ans += 1

print(ans)