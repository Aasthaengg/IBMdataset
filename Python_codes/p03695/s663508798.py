n=int(input())
a=list(map(int, input().split()))
l = [0]*8
c = 0
for i in range(n):
  if a[i] >= 3200:
    c += 1
  else:
    l[a[i]//400] = 1

if l.count(1) == 0:
  print("1 "+str(c))
else:
  print(str(l.count(1))+" "+str(l.count(1)+c))