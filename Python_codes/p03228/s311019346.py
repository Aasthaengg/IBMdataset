a,b,k=map(int,input().split())
count=1
while 1:
    count+=1
    if a%2==1:
        a-=1
    b+=a//2
    a=a//2
    if count>k:
        break
#    print(a,b)
    if b%2==1:
        b-=1
    a+=b//2
    b=b//2
    count+=1
    if count>k:
        break
#    print(a,b)
print(a,b)