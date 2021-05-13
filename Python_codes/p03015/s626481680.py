import time

def pow_k(x, n):
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K = (K*x)%(10**9+7)
        x = (x*x)%(10**9+7)
        n //= 2

    return (K*x)%(10**9+7)

L=input()
N=len(L)


bit=[]
for i in range(0,N):
    if L[N-1-i]=='1':
        bit.append(i+1)

dp=[0 for i in range(0,100001)]

m=bit[0]
if m!=1:
    dp[m]=(2+3**(m-1))%(10**9+7)
else:
    dp[m]=3
time0=time.time()
for i in range(1,len(bit)):
    s=bit[i]
    t=bit[i-1]
    dp[s]=(2*dp[t]+pow_k(3,s-1))
time1=time.time()
print(dp[N]%(10**9+7))