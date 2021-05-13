def main():
    n = int(input())
    p = list(map(int, input().split()))
    p_ascend = [i for i in range(1, n + 1)]
    cnt = 0

    for i in range(n):
        if p[i] != p_ascend[i]:
            cnt += 1

    if cnt == 0 or cnt == 2:
        ans = "YES"
    else:
        ans = "NO"

    print(ans)


if __name__ == "__main__":
    main()
