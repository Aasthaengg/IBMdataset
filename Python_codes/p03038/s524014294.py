n,m=map(int,input().split())
a=sorted(list(map(int,input().split())))
l=sorted([list(map(int,input().split())) for i in range(m)],reverse=True,key=lambda x: x[1])
 
c_l=[]
for b,c in l:
  c_l+=[c]*b
  if len(c_l)>=n:
    break
 
for i in range(min(n,len(c_l))):
  a[i]=max(a[i],c_l[i])
 
print(sum(a))