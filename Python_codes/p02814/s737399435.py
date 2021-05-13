import sys
inout = sys.stdin.readline


def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)


def LCM(a, b):
    return a * b // GCD(a, b)


n, m = map(int, input().split())
a = list(map(int, input().split()))

lcm = 1
for i in a:
    i = i // 2
    lcm = LCM(i, lcm)

for i in a:
    i = i // 2
    if (lcm // i) % 2 == 0:
        print(0)
        sys.exit(0)

ans = ((m // lcm)+1) // 2
print(ans)
