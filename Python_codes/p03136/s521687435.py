n = int(input())
l = list(map(int,input().split()))

maxl = max(l)
maxli = l.index(maxl)
del l[maxli]

if(maxl < sum(l)):
  print("Yes")
else:
  print("No")