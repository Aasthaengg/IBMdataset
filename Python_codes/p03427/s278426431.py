n_=input()
n=int(n_)
l=len(n_)
for i in range(1,17):
    if n+1==(int(n_[0])+1)*10**(l-1):
        ans=0
        while n>0:
            ans+=n%10
            n//=10
        print(ans)
        exit()

n = int(n_[0])*10**(l-1)-1
ans=0
while n>0:
    ans+=n%10
    n//=10
print(ans)