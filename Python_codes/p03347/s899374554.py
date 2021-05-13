def solve(a):
    if a[0][0] != 0:
        return -1
    res = 0
    for aa in a:
        for i in range(len(aa)):
            if i == 0:
                res += aa[i]
            elif aa[i - 1] + 1 == aa[i]:
                res += 1
            elif aa[i - 1] == aa[i]:
                res += aa[i]
            else:
                return -1
    return res


def main():
    n = int(input())
    a = [[]]
    last_a = 0
    for _ in range(n):
        now = int(input())
        if last_a > now:
            a.append([])
        a[-1].append(now)
        last_a = now
    print(solve(a))


if __name__ == '__main__':
    main()
