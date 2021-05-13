N = int(input())
A = list(map(int,input().split()))
x = sum(A)
y = 0
z = []

for n in range(N-1):
  y+=A[n]
  z.append(abs(x-2*y))

print(min(z))