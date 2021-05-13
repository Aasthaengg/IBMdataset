N = int(input())
L = list(int(input()) for i in range(N))
m = 10**9
sum = sum(L)

for l in L:
  if (l%10) != 0:
    m = min(l,m)

if (sum%10) != 0:
  print(sum)
elif (m%10) == 0:
  print(0)
else:
  print(sum-m)