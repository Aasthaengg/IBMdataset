import fractions
n = int(input())
ans = 1
lis = [int(input()) for i in range(n)]
for num in lis:
  ans = (ans * num)//fractions.gcd(ans,num)
print(ans)