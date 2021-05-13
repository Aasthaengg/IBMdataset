a,b=map(int,input().split())
flg=0
for i in range(1001):
    c=int(i*1.08)-i
    d=int(i*1.1)-i
    if c==a and b==d:
        print(i)
        flg=1
        exit()
if flg==0:
    print(-1)

