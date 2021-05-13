n=int(input())
ans=0
a=n//100
b=n//10-(a*10)
c=n%10
if a==1:
    ans+=900
else:
    ans+=100
if b==1:
    ans+=90
else:
    ans+=10
if c==1:
    ans+=9
else:
    ans+=1
print(ans)
