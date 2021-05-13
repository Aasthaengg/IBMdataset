a,b,k=map(int,input().split())
w=0
for i in range(k):
    if i%2==0:
        w=a//2
        a=w
        b+=w
    else:
        w=b//2
        a+=w
        b=w
print(a,b)