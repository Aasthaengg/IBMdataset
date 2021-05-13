n=int(input())
a=[]
for i in range(n):
  a.append(int(input()))
ma=max(a)
if a.count(ma)>1:
  for i in range(n):
    print(ma)

else:
  for i in range(n):
    if a[i]==ma:
      a[i]=0
      print(max(a))
    else:
      print(ma)