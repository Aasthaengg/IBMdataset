n = int(input())
x = list(map(int, input().split()))

m = (n-1)//2
l = sorted(x)
for i in x:
  if i > l[m]: print(l[m])
  else: print(l[m+1])