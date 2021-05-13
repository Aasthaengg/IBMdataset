n=int(input())
a=list(map(int,input().split()))
def f(x):
    ans=0
    while x%2==0:
        ans+=1
        x=x//2
    return ans
print(sum(f(a[i]) for i in range(n)))
