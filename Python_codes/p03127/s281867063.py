n=int(input())
A=[]*n
A[:]=map(int,input().split())

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

ans=0
for i in range(n):
  ans=gcd(ans,A[i])
print(ans)