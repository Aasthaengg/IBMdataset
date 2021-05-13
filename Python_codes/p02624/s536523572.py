def solve():
    n = int(input())

    ans = n * (n+1) - 1

    r = int(n // 2)
    for i in range(2, r+1):
        d = (n // i) * i
        sigma = (d * (d+i))//(2*i) - i
        ans += sigma

    return ans


def main():
    print(solve())


if __name__ == "__main__":
    main()
