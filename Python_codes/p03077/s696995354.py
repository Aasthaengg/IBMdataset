N = int(input())
L = [int(input()) for _ in range(5)]
L.sort()
if N%L[0]:
  ans = N//L[0] + 1 + 4
else:
  ans = N//L[0] + 4
print(ans)