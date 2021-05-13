n=int(input())
p=[int(x) for x in input().rstrip().split()]
l=[i+1 for i in range(n)]
cnt=0
for i in range(n):
  if l[i]!=p[i]:
    cnt+=1
if cnt==2 or cnt==0:
  print("YES")
else:
  print("NO")