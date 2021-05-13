a,b,c=map(int,input().split())
tmpa=0
ampb=0
tmpc=0

if a%2==1 or b%2==1 or c%2==1:
    print(0)
    exit()

for i in range(10**5):
    tmpa=(b+c)/2
    tmpb=(a+c)/2
    tmpc=(b+a)/2
    a=tmpa
    b=tmpb
    c=tmpc
    if a%2==1 or b%2==1 or c%2==1:
        print(i+1)
        exit()
print(-1)