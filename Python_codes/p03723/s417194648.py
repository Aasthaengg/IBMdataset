a,b,c=map(int,input().split())
ct=0
h=0
while 1:
    if (a%2==1)or(b%2==1)or(c%2==1):
        break
    if ct==100000:
        h=1
        break
    a2=a//2
    b2=b//2
    c2=c//2
    a=b2+c2
    b=c2+a2
    c=a2+b2
    ct+=1
if h==1:
    print(-1)
else:
    print(ct)