mod = 10**9+7
n,k = map(int,input().split())
ki = [[]for _ in range(n)]
l = max(n,k)
frac = [1]*(l+1)
for i in range(1,l+1):
    frac[i] = (frac[i-1]*i)%mod
invfrac = [1] *(l+1)
invfrac[-1] = pow(frac[-1],mod-2,mod)
for i in range(l-1,0,-1):
    invfrac[i] = (invfrac[i+1]*(i+1))%mod

def P(x,y):
    return (frac[x]*invfrac[x-y])%mod
    

for i in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    ki[a].append(b)
    ki[b].append(a)

stack = [0]
visited = [0]*n
visited[0] = 1
ans = 1
while stack:
    next = []
    for now in stack:
        visited[now] = 1
        
        if now !=0:
            ans *=P(k-2,len(ki[now])-1)
            if len(ki[now])-1 >= k-1:ans = 0
            
            ans %=mod
        for x in ki[now]:
            if visited[x]:continue
            next.append(x)
    stack = next
ans *= P(k,len(ki[0])+1)
ans %=mod
print(ans)
