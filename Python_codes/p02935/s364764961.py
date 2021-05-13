def solve():
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    x = s[0]
    for i in range(1, n):
        x = (x + s[i]) / 2
    print(x)


solve()
