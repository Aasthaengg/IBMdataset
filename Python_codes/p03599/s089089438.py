a,b,c,d,e,f=map(int,input().split())
inf=float("inf")
a*=100
b*=100
lst=[[inf,0] for _ in range(f//100)]
for i in range(f//b+1):
    for j in range(f//a+1):
        if i==0 and j==0:
            continue
        if (i*b+j*a)<=f:
            lst[(i*b+j*a)//100-1][0]=(i*b+j*a)
sugarlst=[]
C=max(c,d)
D=min(c,d)

for i in range(1500//C+1):
    for j in range((1500-i*C)//D+1):
        sugarlst.append(C*i+D*j)
sugarlst=set(sugarlst)
sugarlst=sorted(sugarlst)

for i in range(f//100):
    if lst[i][0]==inf:
        continue
    for j in sugarlst:
        weight=lst[i][0]+j
        if weight>f or (lst[i][0]//100)*e<j :
            break
        lst[i][1]=j

noudomax=0
for i in lst:
    noudo=i[1]/(i[0]+i[1])
    if noudo>=noudomax:
        ans=i
        noudomax=noudo
if noudomax==0:
    print(a,0)
else:
    print(ans[0]+ans[1],ans[1])