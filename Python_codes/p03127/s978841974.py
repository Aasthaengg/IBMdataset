def gcd(x, y):
  if y==0: return x
  return gcd(y, x%y)

N = int(input())
A = list(map(int, input().split()))
a = A[0]
for i in range(N-1):
  a = gcd(a, A[i+1])
print(a)