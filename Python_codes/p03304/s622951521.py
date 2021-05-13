# soundhound2018-summer-qualC - Ordinary Beauty
def main():
    N, M, D = map(int, open(0).read().split())
    x = 2 if D else 1
    ans = x * (N - D) * (M - 1) / (N * N)
    print(ans)


if __name__ == "__main__":
    main()