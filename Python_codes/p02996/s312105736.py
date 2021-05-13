def main():
    n = int(input())
    ABs = [list(map(int, input().split())) for _ in range(n)]
    ABs = sorted(ABs, key=lambda x: x[1])
    Count = 0
    for AB in ABs:
        Count += AB[0]
        if Count > AB[1]:
            print("No")
            exit()
    print("Yes")


if __name__ == "__main__":
    main()
