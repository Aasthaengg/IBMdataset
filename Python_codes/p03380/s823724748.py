N = int(input())
A = list(map(int, input().split()))

A.sort()

n = A[-1]
r1 = n / 2
temp = 10 ** 9
r = 0

for i, x in enumerate(A):
  if abs(r1 - x) <= temp and i != N-1:
    r = x
    temp = abs(r1 - x)

print(str(n)+" "+str(r))