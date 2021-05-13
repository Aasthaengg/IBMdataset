import sys
n=int(input())
p=list(map(int,input().split()))
sort_p=sorted(p)
q=p
if p==sort_p:
  print("YES")
  sys.exit()
for i in range(1,n):
  for j in range(i):
    p[i],p[j]=p[j],p[i]
    if p==sort_p:
      print("YES")
      sys.exit()
    else:
      p[i],p[j]=p[j],p[i]
print("NO")