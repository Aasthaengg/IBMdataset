import fractions
n=int(input())
a=list(map(int,input().split()))
ans=fractions.gcd(a[0],a[1])
for i in range(2,len(a)):
  ans=fractions.gcd(ans,a[i])
print(ans)