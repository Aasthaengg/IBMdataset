a,b,c,d,e,f=map(int,input().split())
su=[False]*(f+1)
wa=[False]*(f+1)
a*=100
b*=100
e=(100*e)/(100+e)
for i in range(f+1):
    for j in range(f+1):
        if i*c+j*d<=f:
            su[i*c+j*d]=True
        if i*a+j*b<=f:
            wa[i*a+j*b]=True
ans=-1
x,y=a,0
for i in range(1,f+1):
    for j in range(f+1):
        if wa[i] and su[j] and i+j<=f and ans<=100*j/(i+j)<=e:
            ans=100*j/(i+j)
            x,y=i,j
print(x+y,y)