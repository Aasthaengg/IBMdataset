from math import floor
N=int(input())
l=[0]*41
ans=""
for i in range(40,-1,-1):
    #print(i,pow(-2,i),N,N/abs(pow(-2,i)))
    n=abs(N/abs(pow(2,i)))
    if n>=1:
        if N/abs(pow(-2,i))<0:#Nは0未満
            N=N+abs(pow(-2,i))
            if i%2==0:
                l[i]=-1
            else:
                l[i]=1
        else:
            N = N - abs(pow(-2, i))
            if i%2==0:
                l[i]=1
            else:
                l[i]=-1
#print(l)
for i in range(40):
    if l[i]==-1:
        l[i]=1
        l[i+1]=l[i+1]+1
    elif l[i]==2:
        l[i]=0
        l[i+1]=l[i+1]-1
    elif l[i]==-2:
        l[i]=0
        l[i+1]=l[i+1]+1
flag=0
#print(l)
for i in range(40,-1,-1):
    if l[i]==1:
        flag=1
        ans="".join((ans,str(l[i])))
    elif flag==1:
        ans = "".join((ans,str(l[i])))
if len(ans)==0:
    ans="0"
print(ans)