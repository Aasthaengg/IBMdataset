n = int(input())
a = list(map(int, input().split()))

def check(n, a):
    for i in range(n):
        if not a[i*2]==a[i*2+1]:
            return print(0)
    return print((2**n)%(10**9+7))

if len(set(a))==(n+1)//2:
    a = sorted(a)
    if n % 2:
        del a[0]
        check(int((n-1)/2), a)
    else:
        check(int(n/2), a)
else:
    print(0)