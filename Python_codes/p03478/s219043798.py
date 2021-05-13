def int_sum(x):
    y=str(x)
    num=0
    for i in range(len(y)):
        num += x%10
        x = x//10
    return num

n,a,b=map(int,input().split())
ans=0
for i in range(1,n+1):
    if a<=int_sum(i) and int_sum(i)<=b:
        ans +=i
print(ans)