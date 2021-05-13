# soundhound2018-summer-qualC - Ordinary Beauty
def main():
    N, M, D = list(map(int, input().rstrip().split()))
    x = 2 if D else 1
    ans = x * (N - D) * (M - 1) / N ** 2
    print(ans)


if __name__ == "__main__":
    main()