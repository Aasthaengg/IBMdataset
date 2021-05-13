N = int(input())
A = list(map(int, input().split()))
total = 0
maximum = A[0]
for a in A[1:]:
  geta = max(0, maximum - a)
  total += geta
  maximum = a + geta
#  print(a,geta)
print(total)