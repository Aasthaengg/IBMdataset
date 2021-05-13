def main():
    A, B = map(int, input().split())

    if 1 <= A <= 9 and 1 <= B <= 9:
        ans = A * B
    else:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
