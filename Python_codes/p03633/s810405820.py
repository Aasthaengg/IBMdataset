N = int(input())
T = [int(input()) for _ in range(N)]

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

lcm = 1
for t in T:
    lcm *= t // gcd(t, lcm)
print(lcm)
