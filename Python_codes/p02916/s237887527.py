N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
r = 0
p = N
for a in A:
  r += B[a - 1]
  if p == a - 1:
    r += C[p - 1]
  p = a
print(r)