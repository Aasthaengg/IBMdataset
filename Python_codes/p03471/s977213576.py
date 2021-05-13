n,y=map(int,input().split())
num10000=-1
num5000=-1
num1000=-1
for i in range(n+1):
    for j in range(n-i+1):
        k=n-i-j
        if k*1000+j*5000+i*10000==y:
            num1000=k
            num5000=j
            num10000=i
            break
print(num10000,num5000,num1000)