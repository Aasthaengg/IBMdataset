A, B = map(int, input().split())
tmp = 0

if B < A:
  tmp = B
  B = A
  A = tmp

cnt = B
B = B-1

if B < A:
  tmp = B
  B = A
  A = tmp

print(cnt+B)