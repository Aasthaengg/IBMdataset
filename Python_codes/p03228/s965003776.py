a,b,k=map(int,input().split())
for i in range(k//2):
    if a%2==1:a-=1
    a,b=a//2,b+a//2
    if b%2==1:b-=1
    a,b=a+b//2,b//2
if k%2==1:
    if a%2==1:a-=1
    a,b=a//2,b+a//2
print(a,b)