N = int(input())
l2 = 2
l1 = 1
if N == 1:
  ans = 1
else:
  for i in range(N-1):
    l = l2 + l1
    l2 = l1
    l1 = l
  ans = l
print(ans)