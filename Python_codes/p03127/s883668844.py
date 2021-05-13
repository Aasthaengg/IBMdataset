import fractions
n = int(input())
a = list(map(int, input().split()))

a.sort()

mini = a.pop(0)
ans = 10**9+1
for i in range(n-1):
  temp = fractions.gcd(mini, a[i])
  if temp < ans:
    ans = temp
  
print(ans)