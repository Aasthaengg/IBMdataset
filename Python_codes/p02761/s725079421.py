def main():
    n, m = map(int, input().split())
    sc_list = [list(map(int, input().split())) for _ in range(m)]

    for num in range(1000):
        ch = str(num)

        if len(ch) != n:
            continue

        for i in range(m):
            s = sc_list[i][0]
            c = sc_list[i][1]
            if ch[s - 1] != str(c):
                break
        else:
            print(num)
            break
    else:
        print(-1)


if __name__ == "__main__":
    main()
