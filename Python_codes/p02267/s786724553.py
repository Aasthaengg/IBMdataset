def main():
    n = int(input())
    s = list(map(int, input().split()))
    q = int(input())
    t = list(map(int, input().split()))

    cnt = 0
    for et in t:
        sc = s.copy()
        sc.append(et)
        i = 0

        while sc[i] != et:
            i += 1

        if i < n:
            cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()

