n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if sum(a)<sum(b):
    print(-1)
else:
    s=0
    k=[]
    m=0
    for i in range(n):
        d=a[i]-b[i]
        if d>=0:
            k.append(d)
        else:
            m+=d
            s+=1
    k.sort(reverse=True)
    j=0
    while m<0:
        m+=k[j]
        s+=1
        j+=1
    print(s)