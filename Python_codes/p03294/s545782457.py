N = int(input())
A = list(map(int, input().split()))
ans = 0

#最大公約数
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

#最小公倍数
def lcm(x, y):
    return x * y // gcd(x, y)

lcm_A = lcm(A[0], A[1])
for a in A[2:]:
    lcm_A = lcm(lcm_A, a)

for a in A:
    ans += (lcm_A-1) % a

print(ans)
