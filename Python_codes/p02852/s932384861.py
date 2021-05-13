def main():
    N, M = (int(i) for i in input().split())
    S = input()
    from itertools import groupby
    for k, v in groupby(S):
        if k == '1' and len(list(v)) >= M:
            return print(-1)

    ans = []
    i = 0
    S = S[::-1]
    while i <= N:
        cur = M
        while N < i+cur or S[i+cur] == '1':
            cur -= 1
        i += cur
        if cur == 0:
            break
        ans.append(cur)

    ans = ans[::-1]
    print(*ans)


if __name__ == '__main__':
    main()
