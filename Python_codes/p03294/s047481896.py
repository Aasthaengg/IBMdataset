import fractions

N = int(input())
a = list(map(int, input().split()))
l = a[0]
for i in range(1,N):
  l = l * a[i] // fractions.gcd(l, a[i])
m = l-1
fm = 0
for i in range(N):
  fm += m % a[i]
print(fm)