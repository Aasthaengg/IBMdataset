r,g,b,n=map(int,input().split())
cnt=0
for i in range(3001):
    for j in range(3001):
        tmp=n-r*i-g*j
        if tmp>=0 and tmp%b==0:
            cnt+=1
print(cnt)