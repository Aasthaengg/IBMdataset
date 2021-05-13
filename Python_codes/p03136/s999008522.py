n=int(input())
l=list(map(int,input().split()))
sl=sum(l)
flag=True
for i in l:
  if sl-i <= i:
    flag=False
    break
if flag:
  print("Yes")
else:
  print("No")