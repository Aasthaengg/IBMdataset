a=int(input())
b=int(input())
c=int(input())
d=int(input())
ans=0
if a>=b:
    ans+=b*c
    ans+=(a-b)*d
else:
    ans+=a*c
print (ans)