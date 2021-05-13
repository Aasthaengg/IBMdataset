N,M = map(int,input().split())

def fib(n):
    if n == 0:
        return 0
    one = 1
    two = 1
    for _ in range(n-2):
        two,one = one + two,two
    return two

ans,now = 1,0
for i in range(M):
    a = int(input())
    ans *= fib(a - now)
    now = a+1
    if ans > 10**9+7:
        ans %= 10**9 + 7
ans *= fib(N - now + 1)
ans %= 10**9 + 7

print(ans)