n,k = map(int,input().split())
mod = 10**9+7
a = list(map(int,input().split()))
c = [0]*n
b = []
import bisect
for i in range(n-1,-1,-1):
    c[i] = bisect.bisect_left(b,a[i])
    bisect.insort_left(b,a[i])
    
ans = 0
for i in c:
    ans += i*k

for i in range(n):
    c[i] = bisect.bisect_left(b,a[i])
    
sk = k*(k-1)//2
for i in c:
    ans += i*sk

print(ans%mod)