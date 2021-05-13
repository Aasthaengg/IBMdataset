def solve():
    n = int(input())

    ans = (n * (n+1))//2

    for i in range(2, n+1):
        d = (n // i) * i
        sigma = (d * (d+i))//(2*i)
        ans += sigma

    return ans


def main():
    print(solve())


if __name__ == "__main__":
    main()
