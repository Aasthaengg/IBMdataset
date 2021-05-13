n=3
a=[0]*n
a[:]=map(int,input().split())
a.sort()
#print(a)
if sum(a)==2*a[n-1]:
  print("Yes")
else:
  print("No")