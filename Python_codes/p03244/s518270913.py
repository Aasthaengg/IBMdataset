n=int(input())
v=list(map(int,input().split()))
d1={}
d2={}
l1=[]
l2=[]
for i in range(n):
    num=v[i]
    if i%2==0:
        try:
            d1[num]+=1
        except:
            d1[num]=1
    else:
        try:
            d2[num]+=1
        except:
            d2[num]=1
for i in d1:
    l1.append([d1[i],i])
for i in d2:
    l2.append([d2[i],i])
l1.sort(reverse=True)
l2.sort(reverse=True)
ans=n
if l1[0][1]!=l2[0][1]:
    ans-=(l1[0][0]+l2[0][0])
elif len(l1)==1 and len(l2)==1:
    ans//=2
elif len(l1)==1:
    ans-=l2[1][0]
elif len(l2)==1:
    ans-=l1[1][0]
else:
    a=ans-l1[0][0]-l2[1][0]
    b=ans-l1[1][0]-l2[0][0]
    ans=min(a,b)
print(ans)
