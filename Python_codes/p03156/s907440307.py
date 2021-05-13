n=int(input())
a,b=map(int,input().split())
p=list(map(int,input().split()))
num1=0
num2=0
num3=0
for i in range(n):
    if p[i]<=a:
        num1+=1
    elif p[i]<=b:
        num2+=1
    else:
        num3+=1
print(min(num1,num2,num3))
