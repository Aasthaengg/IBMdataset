x=sorted(list(map(int,input().split())))
a=x[0]
b=x[1]
c=x[2]
ans=0
ans+=c-b
b=c
a+=ans
if (c-a)%2==0:
    ans+=(c-a)//2
else:
    ans+=(c-a+1)//2+1
print(ans)

