def resolve():
    n = int(input())
    ab = list(list(map(int, input().split())) for _ in range(n))
    ab.sort()
    ans = ab[-1][0] + ab[-1][1]
    print(ans)


if __name__ == "__main__":
    resolve()
