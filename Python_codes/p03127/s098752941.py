def gcd(a, b):
    if b==0:    return a
    return gcd(b, a%b)



n=int(input())
A=list(map(int, input().split()))

ans=gcd(A[0], A[1])

for i in range(2, n):
    ans=gcd(ans, A[i])

print(ans)