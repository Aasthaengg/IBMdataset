n,a,b=map(int,input().split())
def f(x):
    m=0
    while x>0:
        m+=x%10
        x=x//10
    return m
ans=0
for i in range(n):
    
    if a<=f(i+1)<=b:
        ans+=i+1
print(ans)
    
