A, B = [int(i) for i in input().split()]
if B % A == 0:
  ans = A + B
else:
  ans = B - A
print(ans)
