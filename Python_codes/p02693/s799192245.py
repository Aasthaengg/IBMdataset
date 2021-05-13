def main():
    K = int(input())
    A, B = map(int, input().split())

    if B // K * K >= A:
        ans = "OK"
    else:
        ans = "NG"

    print(ans)


if __name__ == "__main__":
    main()
