f=lambda x:x if p[x]<0else f(p[x])
def u(x,y):
  x,y=f(x),f(y)
  if x!=y:
    if p[x]>p[y]:x,y=y,x
    p[x]+=p[y]
    p[y]=x
h,*s=open(0)
h,w=map(int,h.split())
r=range(h*w)
p=[-1]*h*w
for i in r:
  j,k=i//w,i%w
  h>j+1and s[j][k]!=s[j+1][k]and u(i,i+w)or w>k+1and s[j][k]!=s[j][k+1]and u(i,i+1)
d=[[0,0]for _ in r]
for i in r:d[f(i)][s[i//w][i%w]<'.']+=1
print(sum(i*j for i,j in d))