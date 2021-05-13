x=int(input())
ans,mod=divmod(x,11)
ans*=2
if mod>6:
    ans+=2
elif mod>0:
    ans+=1
print(ans)