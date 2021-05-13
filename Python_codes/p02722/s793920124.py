
N = int(input())


def solve(num):
    ret = set()

    p = 1
    while p * p <= num:
        if num % p == 0:
            ret.add(p)
            ret.add(num // p)
        p += 1

    return ret


s1 = solve(N)
s2 = solve(N-1)



# 1は答えに入らないので抜いた
ans = len(s2) - 1
for n in s1:
    if n == 1:
        continue
    tmp = N
    while tmp % n == 0:
        tmp = tmp // n
    if tmp % n == 1:
        ans += 1


print(ans)