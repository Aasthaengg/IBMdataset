n,k = map(int,input().split())
r,s,p = map(int,input().split())
t=input()
l=["" for i in range(n)]

ans=0
for i in range(k):
  if t[i]=="r":
    l[i]="p"
    ans+=p
  elif t[i]=="p":
    l[i]="s"
    ans+=s
  else:
    l[i]="r"
    ans+=r

for i in range(k,n):
  if t[i]=="r":
    if l[i-k]!="p":
      l[i]="p"
      ans+=p

  elif t[i]=="p":
    if l[i-k]!="s":
      ans+=s
      l[i]="s"

  else:
    if t[i]=="s":
      if l[i-k]!="r":
        ans+=r
        l[i]="r"

print(ans)
