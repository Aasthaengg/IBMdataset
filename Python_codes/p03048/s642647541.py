a,b,c,d=map(int,input().split())
ans=0
for i in range(d//a+1):
    for j in range((d-i*a)//b+1):
        if (d-i*a-j*b)%c==0:
            ans+=1
print(ans)