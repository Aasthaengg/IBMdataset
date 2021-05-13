n,k=map(int,input().split())
s=input()
d=[]
f=True

if "0" not in s:
  print(n)
  exit()
if s[0]=="0":
    d.append(0)
    f=False

seq=1
for i in range(1,n):
    if s[i]=="0" and not f:
        seq+=1
    elif s[i]=="0" and f:
        f=False
        d.append(seq)
        seq=1
    elif s[i]=="1" and f:
        seq+=1
    else:
        f=True
        d.append(seq)
        seq=1
    if i==n-1:
      d.append(seq)
if s[-1]=="0":
    d.append(0)
l=len(d)
res=[0]*(l+1)
res[0]=0
for i in range(1,l+1):
    res[i]=res[i-1]+d[i-1]
ans=1
for i in range(1,l+1):
    if i%2==1:
        continue
    if 2*k+i-1>l:
      a=res[l]-res[i-2]
    else:
      a=res[2*k+i-1]-res[i-2]
    if a>ans:
        ans=a
print(ans)
