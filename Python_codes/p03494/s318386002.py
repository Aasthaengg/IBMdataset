
n=int(input())
a=list(map(int,input().split()))
def f(x):
    m=0
    while x%2==0:
        m+=1
        x=x//2
    return m
print(min(f(a[i]) for i in range(n)))
