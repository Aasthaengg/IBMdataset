def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr
  
n,m = map(int,input().split())
chk = factorization(m)
from scipy.misc import comb

mod = 10**9+7
ans = 1
if m > 1:
  for i in chk:
    ans *= comb(i[1]+n-1,i[1],mod)
    ans %= mod
print(ans)