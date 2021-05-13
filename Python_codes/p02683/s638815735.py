import math
def facts(n):
    ans = []
    for  i in range(1, int(math.sqrt(n)+1)):
        if(n%i==0):
            ans.append(i)
            ans.append(n//i)
    ans = sorted(ans)
    return ans


n,m, x = map(int, input().split())
arr = []
narr = [0 for i in range(m)]
ans = 123456789
for i in range(n):
    tarr = list(map(int, input().split()))
    arr.append(tarr)
for i in range(1<<n):
    tarr = list(narr)
    cost = 0
    for a in range(n):
        if((i>>a)&1):
            cost+=arr[a][0]
            for b in range(1, m+1):
                tarr[b-1] += arr[a][b]
    ok = True
    for i in range(m):
        if(tarr[i]<x):
            ok = False
            break
    if(ok):
        ans = min(ans, cost)
if(ans == 123456789):
    print(-1)
else:
    print(ans)
