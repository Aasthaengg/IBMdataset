from fractions import gcd
N = int(input())
an = list(map(int, input().split()))


def lcm(x, y):
    return (x * y) // gcd(x, y)


temp = lcm(an[0], an[1])
for i in range(2, N):
    temp = lcm(temp, an[i])
ans = 0
for a in an:
    ans += (temp-1) % a
print(ans)
