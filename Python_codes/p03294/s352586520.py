import fractions
n=int(input())
a=list(map(int, input().split()))
ans=a[0]
for i in range(1,n):
    ans = ans * a[i] // fractions.gcd(ans, a[i])
tmp=0
for j in range(n):
  tmp+=(ans-1)%a[j]
print(tmp)