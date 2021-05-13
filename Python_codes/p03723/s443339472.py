a,b,c=map(int,input().split())
for i in range(500000):
    if a%2==1 or b%2==1 or c%2==1:
        print(i);exit()
    
    else:
      p=(b+c)//2 ;q=(a+c)//2 ; r=(a+b)//2
      a=p ; b=q;c=r
else:
    print(-1)