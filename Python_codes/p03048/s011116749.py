r,g,b,n=map(int,input().split())
maxr=n//r
maxg=n//g
maxb=n//b
bag=0
cnt=0
for i in range(0,maxr+1):
    bag+=i*r
    for j in range(0,((n-bag)//g)+1):
        bag+=j*g
        if (n-bag)%b==0:
            cnt+=1
        bag=i*r
    bag=0
print(cnt)