from math import sqrt

n = int(input())

ans = 0


def judge(x):
    global n
    if x == 0:
        return False
    return n // x == n % x


for i in range(1, int(sqrt(n)) + 1):
    if n % i == 0:
        if judge(i-1):
            ans += i-1
        if judge(n // i - 1):
            ans += n // i - 1

print(ans)
