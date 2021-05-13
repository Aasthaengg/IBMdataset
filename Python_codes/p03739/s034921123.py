n=int(input())
l=list(map(int,input().split()))
s=0
a=0
for i in range(n):
    s+=l[i]

    if i%2:
        if s<=0:
            a+=1-s
            s=1
    else:
        if s>=0:
            a+=s+1
            s=-1

b=0;s=0
for i in range(n):
    s+=l[i]
    if i%2==0:
        if s<=0:
            b+=1-s
            s=1
    else:
        if s>=0:
            b+=s+1
            s=-1
print(min(a,b))