def main():
    # s = int(input())
    # n, k = map(int, input().split())
    # h = list(map(int, input().split()))
    # s = input()

    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    total = 0
    li = [a, b, c, d, e]
    mini = 10**10
    ans_idx = 0
    for i, s in enumerate(li):
        last_s = int(str(s)[-1])
        if mini > last_s and last_s != 0:
            mini = last_s
            ans_idx = i

    for i, s in enumerate(li):
        if i != ans_idx:
            if s % 10 != 0:
                total += s // 10 * 10 + 10
            else:
                total += s
        else:
            total += s

    print(total)


if __name__ == '__main__':
    main()
