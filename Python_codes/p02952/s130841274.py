N=int(input())
arr=[]

a=N
while a>0:
    arr.append(a%10)
    a=a//10

keta=len(arr)

ans=0
for i in range(1,keta):
    if i%2==1:
        ans+=9*10**(i-1)
if keta%2==0:
    print(ans)
else:
    print(ans+N-(10**(keta-1)-1))
