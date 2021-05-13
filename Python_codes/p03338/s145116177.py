ans=0
N=int(input())
l=list(input())
for i in range(1,N):
   tmp1=set(l[0:i])
   tmp2=set(l[i:])
   tmp3=[]
   tmp3.append(list(tmp1))
   tmp3.append(list(tmp2))
   tmp3=sum(tmp3,[])
   tmp3=set(tmp3)
   ans=max(ans,-len(tmp3)+len(tmp2)+len(tmp1))
print(ans)