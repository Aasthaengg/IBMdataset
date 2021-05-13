r,d,x=map(int,input().split())

count=0
while count<=9:
    x=r*x-d
    print(x)
    count+=1

