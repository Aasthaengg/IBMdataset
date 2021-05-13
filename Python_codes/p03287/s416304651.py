n,m = map(int,input().split())
ai = [int(i) for i in input().split()]

for i in range(n):
    ai[i] = ai[i]%m

a = [0]*(n+1)
tmp = 0

for i in range(n):
    tmp += ai[i]
    tmp %= m
    a[i+1] = tmp
    
ans = 0

#li = [0]*(m)

d = dict()

for i in range(n+1):
    if a[i] in d:
        ans += d[a[i]]
        d[a[i]] += 1
    else:
        d[a[i]] = 1
    #print(ans,d)

print(ans)
