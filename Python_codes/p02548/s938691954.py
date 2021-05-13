def solve1():
    n = int(input())
    a, b, c = 1, 1, 1
    ans = 0

    while n >= c:
        while b <= (n-c):
            ans += (n-c)//b
            b += 1
        c += 1

    print(ans)


def solve2():
    n = int(input())
    ans = 0

    for i in range(1, n):
        ans += (n-1)//i

    print(ans)


solve2()
