N = int(input())
#A = list(reversed(sorted(list(map(int, input().split())))))
A = sorted(list(map(int, input().split())))
assert len(A) == N
mul = 1
for a in A:
  mul *= a
#  print(a, mul)
  if a == 0:
    print(0)
    break
  if mul > (10 ** 18):
    print(-1)
    break
else:
  print(mul)