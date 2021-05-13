n = int(input())
l0=2
l1 = 1
l = l0 + l1
for i in range(n-2):
    l0 = l1
    l1 = l
    l = l0 + l1
if n==1:
  print(l1)
else:
  print(l)
