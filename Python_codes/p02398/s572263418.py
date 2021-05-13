a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
ans=0
for i in range(a,b+1) :
    if c%i==0 :
        ans+=1
print("{}".format(ans))
