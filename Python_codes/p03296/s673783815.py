def main():
    N = int(input())
    A = list(map(int, input().split()))
    prev = 0
    ans = 0
    for a in A:
        if a == prev:
            ans += 1
            prev = 0
        else:
            prev = a
    print(ans)


if __name__ == "__main__":
    main()
