n,a,b=map(int,input().split())
def func(x):
    count=0
    while True:
        count+=x%10
        x//=10
        if x==0:
            break
    return count
ans=0
for i in range(n+1):
    if func(i)>=a and func(i)<=b:
        ans+=i
print(ans) 
