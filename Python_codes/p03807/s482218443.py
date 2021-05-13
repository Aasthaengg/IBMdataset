n=int(input())
cnt=0
a=list(map(int,input().split()))
for i in a:
  if i%2==1:
    cnt=1-cnt
if cnt==0:
  print("YES")
else:
  print("NO")