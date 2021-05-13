t,a,k=list(map(int,input().split()))
i=0
while True:
    if t%2==1:
        t-=1
    a+=t//2
    t-=t//2
    i+=1
    if i>=k:
        break
    if a%2==1:
        a-=1
    t+=a//2
    a-=a//2
    i+=1
    if i>=k:
        break

print(t,a)