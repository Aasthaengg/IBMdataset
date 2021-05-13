import math
def facts(n):
    ans = []
    for  i in range(1, int(math.sqrt(n)+1)):
        if(n%i==0):
            ans.append(i)
            ans.append(n//i)
    ans = sorted(list(dict.fromkeys(ans)))
    if(ans[-1]==n):
        ans = ans[:-1]
    return ans


n, m,k  = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
pa  = [0]
pb = [0]
ans = 0
for i in range(n):
    pa.append(a[i]+pa[i])
for i in range(m):
    pb.append(b[i]+pb[i])
for c in range(n+1):
    if(pa[c] > k):
        break
    else:
        while(pb[m] > k-pa[c]):
            m-=1
        ans = max(ans, c+m)
            
print(ans)