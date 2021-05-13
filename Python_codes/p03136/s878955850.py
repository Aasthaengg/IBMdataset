n=int(input())
l=list(map(int,input().split()))
a=max(l)
b=0
for i in range(n):
  b+=l[i]
b=b-a
if a<b:
  print("Yes")
else:
  print("No")