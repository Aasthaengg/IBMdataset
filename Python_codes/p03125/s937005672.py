def solve(a, b):
    if b % a == 0:
        return b + a
    else:
        return b - a


def main():
    a, b = map(int, input().split())

    ans = solve(a, b)
    print(ans)


main()
