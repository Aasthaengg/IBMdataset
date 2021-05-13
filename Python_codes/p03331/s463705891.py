def main():
    N = int(input())

    ans = 100000

    for i in range(1, N):
        tmp = sum(map(int, str(i)))
        tmp += sum(map(int, str(N-i)))
        if tmp < ans:
            ans = tmp

    print(ans)


if __name__ == "__main__":
    main()
