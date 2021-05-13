def solve():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n-1):
        now = i
        if p[now - 1] < p[now] < p[now + 1]:
            count += 1
        elif p[now + 1] < p[now] < p[now - 1]:
            count += 1
    print(count)


if __name__ == '__main__':
    solve()
