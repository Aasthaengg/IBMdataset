n,m=map(int,input().split())
itv=[]
for i in range(m):
  a,b=map(int,input().split())
  itv+=[(b,a)]
itv=sorted(itv)
cnt=0
l=1
for t,s in itv:
  if l<=s:
    l=t
    cnt+=1
print(cnt)