n=int(input())
l=[input() for i in range(3)]
ans=0
for i in range(n):
  a=set([l[0][i],l[1][i],l[2][i]])
  ans+=len(a)-1
print(ans)