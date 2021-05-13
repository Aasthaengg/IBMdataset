a, b, c = map(int,input().split())

if a%2!=0 or b%2!=0 or c%2!=0:
    print(0)
    exit()

if a==b==c:
    print(-1)
    exit()

times=0
while a%2==0 and b%2==0 and c%2==0:
    times+=1
    a_=a//2
    b_=b//2
    c_=c//2
    a=b_+c_
    b=a_+c_
    c=a_+b_

print(times)