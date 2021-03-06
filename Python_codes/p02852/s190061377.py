def main():
    n, m = map(int, input().split())
    s = input()
    ss = s[::-1]
    if n <= m:
        print(n)
    else:
        cnt = 0
        for i in range(n + 1):
            if s[i] == "1":
                cnt += 1
            else:
                cnt = 0
            if cnt >= m:
                print(-1)
                exit()
        pos = 0
        res = []
        while n != pos:
            for i in reversed(range(m + 1)):
                if pos + i > n:
                    continue
                if ss[pos + i] != "1":
                    pos += i
                    res.append(i)
                    break
        print(*res[::-1])


if __name__ == '__main__':
    main()
