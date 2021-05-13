def solve():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    count = 1
    for i in range(1, n+1):
        d = d + l[i-1]
        if d > x:
            print(count)
            exit()
        count += 1
    print(count)


if __name__ == '__main__':
    solve()
