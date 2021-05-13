a,b,c=map(int,input().split())
count=0
if a==b==c and a%2==0:
    print(-1)
    exit()
while a%2==0 and b%2==0 and c%2==0:
    A=a//2
    B=b//2
    C=c//2
    a=B+C
    b=C+A
    c=A+B
    count+=1
print(count)