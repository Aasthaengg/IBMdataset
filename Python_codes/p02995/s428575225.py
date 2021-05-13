from math import gcd 
a, b, c, d = map(int, input().split())
n = b-a+1

def lcm(a, b):
    return a * b // gcd(a, b)

def cal(x, a, b):
    cnt = b//x - a//x
    if a%x == 0:
        cnt += 1
    return cnt

ans = cal(c, a, b)
ans += cal(d, a, b)
ans -= cal(lcm(c, d), a, b)
print(n - ans)
