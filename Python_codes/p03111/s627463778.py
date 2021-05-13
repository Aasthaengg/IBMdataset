n,A,B,C=map(int,input().split())
L=[0]*n
for i in range(n):
  L[i]=int(input())
ans=10**10
for i in range(2**n):
  S=format(i,"10b")
  K=[]
  for j in range(n):
    if S[-1-j]=="1":
      K.append(j)
  k=len(K)
  if len(K)<3:
    continue
  for j in range(2**k):
    SS=format(j,"10b")
    AA=[]
    for l in range(k):
      if SS[-1-l]=="1":
        AA.append(K[l])
    a=len(AA)
    if a<1 or k-2<a:
      continue
    KK=sorted(list(set(K)-set(AA)))
    kk=k-a
    for l in range(2**kk):
      SSS=format(l,"10b")
      BB=[]
      for m in range(kk):
        if SSS[-1-m]=="1":
          BB.append(KK[m])
      b=len(BB)
      if b<1 or kk-1<b:
        continue
      CC=sorted(list(set(KK)-set(BB)))
      c=len(CC)
      AAA=sum(L[AA[x]] for x in range(a))
      BBB=sum(L[BB[x]] for x in range(b))
      CCC=sum(L[CC[x]] for x in range(c))
      aans=(a+b+c-3)*10+abs(AAA-A)+abs(BBB-B)+abs(CCC-C)
      if aans<ans:
        ans=aans
print(ans)