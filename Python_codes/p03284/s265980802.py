ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n,k= nm()

if n%k==0:
    print(0)
else:
    print(1)