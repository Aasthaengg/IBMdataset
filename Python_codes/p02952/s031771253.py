n=input()
ans=0
if len(n)==1:
    ans+=int(n)
elif len(n)%2==1:
    ans+=int(n)-10**(len(n)-1)+1
for i in range(1,len(n),2):
    ans+=9*10**(i-1)
print(ans)