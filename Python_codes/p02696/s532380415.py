def solve(a, b, n):
    return a * min(b-1, n) // b - a * (min(b-1, n) // b)


def solve_baka(a, b, n):
    ans = -1e9
    for x in range(n+1):
        ans = max((a * x) // b - a * (x//b), ans)
        print('    ', x, (a * x) // b - a * (x//b))
    return ans


def main():
    a, b, n = [int(v) for v in input().split()]
    print(solve(a, b, n))


if __name__ == '__main__':
    main()
