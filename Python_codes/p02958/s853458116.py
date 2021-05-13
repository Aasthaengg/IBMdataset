n=int(input())
p=[int(x) for x in input().split()]
P=sorted(p)
cnt=0
for i in range(n):
  if p[i]!=P[i]:
    cnt+=1
if cnt==0 or cnt==2:
  print("YES")
else:
  print("NO")