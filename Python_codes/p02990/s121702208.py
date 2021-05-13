N = 1000000007

def fac(n,r,N):
    ans=1
    for i in range(r):
        ans=ans*(n-i)%N
    return ans

def combi(n,r,N):
    if n<r or n<0 or r<0:
        ans = 0
        return ans
    r= min(r, n-r)
    ans = fac(n,r,N)*pow(fac(r,r,N),N-2,N)%N
    return ans


n , k = map(int, input().split())

for i in range(1,k+1):
    print(combi(k-1,i-1,N)*combi(n-k+1,i,N)%N)
