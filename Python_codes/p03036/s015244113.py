r,d,x=map(int,input().split())
count=0
num=x
for i in range(10):
    count=num*r-d
    num=count
    print(num)
