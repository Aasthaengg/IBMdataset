n,k=map(int,input().split())
r,s,p=map(int,input().split())
t=str(input())
t=list(t)
a=[0]*n
ans=0
for i in range(k):
  if t[i]=="r":
    ans=ans+p
    a[i]="r"
  if t[i]=="s":
    ans=ans+r
    a[i]="s"
  if t[i]=="p":
    ans=ans+s
    a[i]="p"
for i in range(k,n):
  if t[i]!=a[i-k]:
    if t[i]=="r":
      ans=ans+p
      a[i]="r"
    if t[i]=="s":
      ans=ans+r
      a[i]="s"
    if t[i]=="p":
      ans=ans+s
      a[i]="p"
print(ans)    