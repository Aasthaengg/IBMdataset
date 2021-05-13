n,k=list(map(int,input().split()))
r,s,p=list(map(int,input().split()))
t=list(input())
cnt=0
u=[]
for i in range(n):
  if t[i]=='r':
    u.append("p")
  elif t[i]=='s':
    u.append("r")
  else:
    u.append("s")

for i in range(n):
  if u[i]=="r":
    if i<k:
      cnt+=r
    else:
      if u[i-k]=="r":
        cnt+=0
        u[i]="#"
      else:
        cnt+=r

  elif u[i]=="s":
    if i<k:
      cnt+=s
    else:
      if u[i-k]=="s":
        cnt+=0
        u[i]="#"
      else:
        cnt+=s

  elif u[i]=="p":
    if i<k:
      cnt+=p
    else:
      if u[i-k]=="p":
        cnt+=0
        u[i]="#"
      else:
        cnt+=p
#print("".join(u))
print(cnt)