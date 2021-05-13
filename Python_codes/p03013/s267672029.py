def Fib(n):
    a, b = 0, 1
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(n-2):
            a, b = b, a + b
        return b

def solve():
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(m)]

    if m > 1:
        for i in range(m-1):
            if a[i+1]-a[i] <= 1:
                return 0
    elif m == 0:
        return Fib(n+2)%1000000007

    
    a = a + [n]
    l = [a[0]]
    for i in range(1, m):
        l.append(a[i]-a[i-1]-1)
    l = l + [a[-1]-a[-2]]
    ans = 1
    for i in l:
        ans *= Fib(i+1)

    return ans%1000000007


print(solve())