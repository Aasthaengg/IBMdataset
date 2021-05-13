n=int(input())
t=list(map(int,input().split()))
sumt=sum(t)
m=int(input())
ans=[]
for i in range(m):
  p,x=map(int,input().split())
  ans.append(sumt-t[p-1]+x)
print(*ans, sep="\n")