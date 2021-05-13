def main():
    N = int(input())
    transportation = [int(input()) for _ in range(5)]

    time = [0] * 5

    for i in range(5):
        if N % transportation[i] == 0:
            time[i] = N // transportation[i]
        else:
            time[i] = N // transportation[i] + 1

    ans = max(time) + 4

    print(ans)


if __name__ == "__main__":
    main()
