x,n=map(int,input().split())
p=list(map(int,input().split()))
num1=0
num2=0
if(n==0):
    print(x)
    exit()
for i in range(100):
    num1=x-i
    num2=x+i
    if(not num1 in p and not num2 in p):
        print(num1)
        exit()
    elif(not num2 in p):
        print(num2)
        exit()
    elif(not num1 in p):
        print(num1)
        exit()