def main():
    n = int(input())
    a = list(map(int, input().split()))

    a.append(0)

    ans = 0
    cnt = 1
    for i in range(n):
        if a[i] == a[i+1]:
            cnt += 1
        else:
            ans += cnt // 2
            cnt = 1

    print(ans)


if __name__ == "__main__":
    main()
