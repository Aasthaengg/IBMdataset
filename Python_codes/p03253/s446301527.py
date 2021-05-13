from math import factorial

N,M=list(map(int, input().split()))
C=10**9+7
def factorization(n):
    if n==1:
        return [[1,1]]
    temp=n
    ans=[]
    for i in range(2, int(n**0.5+1.01)):
        if temp % i ==0:
            ct=0
            while temp % i == 0:
                temp //= i
                ct += 1
            ans.append([i, ct])
    if temp != 1:
        ans.append([temp, 1])
    return ans

L=factorization(M)
# print(L)
# n種類のモノから重複を許してk個選ぶ重複組合せは
# モノk個と仕切りn-1個の順列だから
# (n+k-1)!/k!(n-1)!

ans=1
for i in L:
    if i[0]!=1:
        tmp=(factorial(i[1]+N-1) // (factorial(i[1])*factorial(N-1)))
        # print(tmp)
        ans*=tmp
        ans%=C
print(ans)