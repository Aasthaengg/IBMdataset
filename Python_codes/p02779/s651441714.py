n=int(input())
a=[int(x) for x in input().split()]


ans={}
flag=0
for i in a:
  if i not in ans:
    ans[i]=1
  else:
    flag=1
    break

if flag==1:
  print("NO")
else:
  print("YES")