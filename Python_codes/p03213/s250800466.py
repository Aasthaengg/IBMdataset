import math
N=int(input())
pl=[2]
for i in range(3,N+1):
  if all(i%p!=0 for p in pl):
    pl.append(i)
pd={}
Nf=math.factorial(N)
for i in range(len(pl)):
  if Nf%pl[i]==0:
    pd[pl[i]]=1
    Nf//=pl[i]
    while Nf%pl[i]==0:
      pd[pl[i]]+=1
      Nf//=pl[i]
l74=[]
l24=[]
l14=[]
l4=[]
l2=[]
for i in range(len(pd)):
  if pd[pl[i]]>=74:
    l74.append(pl[i])
  if pd[pl[i]]>=24:
    l24.append(pl[i])
  if pd[pl[i]]>=14:
    l14.append(pl[i])
  if pd[pl[i]]>=4:
    l4.append(pl[i])
  if pd[pl[i]]>=2:
    l2.append(pl[i])
ans1=len(l74)
ans2=len(l24)*(len(l2)-1) if len(l2)>=1 else 0
ans3=len(l14)*(len(l4)-1) if len(l4)>=1 else 0
ans4=(len(l4)-1)*len(l4)*(len(l2)-2)//2 if len(l2)>=2 else 0
print(ans1+ans2+ans3+ans4)