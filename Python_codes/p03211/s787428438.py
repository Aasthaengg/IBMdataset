def solve():
    N = input()
    target = 753
    ans = 1000
    for i in range(len(N)-2):
        ans = min(ans, abs(753-int(N[i:i+3])))

    print(ans)


if __name__ == '__main__':
    solve()