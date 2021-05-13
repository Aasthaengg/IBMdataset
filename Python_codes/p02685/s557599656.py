n,m,k = map(int, input().split())

N = 998244353

factorial = [1]
inverse = [1]
for i in range(1, n+2):
    factorial.append(factorial[-1] * i % N)
    inverse.append(pow(factorial[-1], N - 2, N))

def combi(n, r):
    if n < r or r < 0:
        return 0
    elif r == 0:
        return 1
    return factorial[n] * inverse[r] * inverse[n - r] % N

ans=0
if k<n//2:
    for i in range(k+1):
        ans+=m*combi(n-1,i)*pow(m-1,n-1-i,N)%N
        ans%=N
    print(ans)
else:
    for i in range(k+1,n):
        ans+=m*combi(n-1,i)*pow(m-1,n-1-i,N)%N
        ans%=N
    ans = pow(m,n,N)-ans
    if ans < 0:
        ans +=N
    print(ans)
