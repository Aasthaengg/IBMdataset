import math
n=int(input())
num=int(math.sqrt(n*2))
num2=(num*(num+1))//2
num3=n-num2
if num3>num:
    num+=1
    num3-=num
if num3<0:
    num-=1
    num3+=num+1
ans=list(range(1,num+1))
for i in range(num3):
    ans[-i-1]+=1
for i in ans:
    print(i)
