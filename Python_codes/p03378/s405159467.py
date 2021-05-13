def main():
    n, m, x = map(int, input().split())
    a_list = list(map(int, input().split()))
    cnt = 0

    for a in a_list:
        if a < x:
            cnt += 1
        if x < a:
            break

    print(min(cnt, m - cnt))


if __name__ == "__main__":
    main()
