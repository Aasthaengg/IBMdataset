N = int(input())
A = list(map(int, input().split()))

def f(n):
    ret = 0
    while n % 2 == 0:
        n //= 2
        ret += 1
    return ret

ans = 0
for a in A:
    ans += f(a)
print(ans)

