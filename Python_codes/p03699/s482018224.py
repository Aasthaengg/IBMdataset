def main():
    n = int(input())
    ss = sorted([int(input()) for _ in range(n)])
    ans = sum(ss)
    Count = 0
    if ans % 10 == 0:
        for i in range(n):
            if ss[i] % 10 != 0:
                ans -= ss[i]
                break
            else:
                Count += 1

    if Count == n:
        ans = 0
    print(ans)


if __name__ == "__main__":
    main()
