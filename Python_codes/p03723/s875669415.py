a,b,c = map(int,input().split())
acnt = 0
bcnt = 0
ccnt = 0
cnt = 0
if a == b and a== c and a%2 == 0:
    print(-1)
    exit()
while a%2 == 0 and b%2 == 0 and c%2 == 0:
    cnt += 1
    acnt = (b+c)//2
    bcnt = (a+c)//2
    ccnt = (a+b)//2
    a = acnt
    b = bcnt 
    c = ccnt
print(cnt)
