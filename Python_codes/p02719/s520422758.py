n,k=map(int,input().split())
ok=0
n=n%k
def f(x):
    if abs(x-k)<x:
        f(abs(x-k))
    else:
        print(x)
f(n)