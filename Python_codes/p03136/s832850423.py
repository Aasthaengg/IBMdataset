n = int(input())
Mlist = sorted(list(map(int,input().split())))[::-1]
if Mlist[0] >= sum(Mlist[1:]):
  print("No")
else:
  print("Yes")