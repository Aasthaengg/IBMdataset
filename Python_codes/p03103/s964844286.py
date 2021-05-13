def main():
    n, m = map(int, input().split())
    ab_list = [list(map(int, input().split())) for _ in range(n)]
    ab_list.sort(key=lambda x: x[0])
    ans, cnt = 0, 0

    for i in range(n):
        ans += ab_list[i][0] * ab_list[i][1]
        cnt += ab_list[i][1]
        if cnt > m:
            ans -= ab_list[i][0] * (cnt - m)
            break

    print(ans)


if __name__ == "__main__":
    main()
