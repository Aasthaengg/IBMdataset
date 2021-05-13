n=int(input())
x=list(map(int,input().split()))
num=sorted(x)
num1=num[n//2-1]
num2=num[n//2]
for i in range(n):
    if x[i]<=num1:
        print(num2)
    else:
        print(num1)
