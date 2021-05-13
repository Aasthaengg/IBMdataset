n,k=map(int, input().split())
mod = 10**9 + 7
ans = [0]*k
import math
ans[0]=(math.factorial(2+n-k-1) // (math.factorial(2+n-k-1-n+k) * math.factorial(n-k))) %mod

for i in range(1,k):#iは仕切りの数
    spl = math.factorial(k-1) // (math.factorial(k-1- i) * math.factorial(i))#仕切りのパターン
    rest = n-k-i
    if rest < 0:
        break
    if rest == 0:
        ans[i] = spl%mod
    else:
        ans[i] = (spl*(math.factorial(2+i+rest-1) // (math.factorial(2+i-1) * math.factorial(rest))))%mod
for i in ans:
    print(i)