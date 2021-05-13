def main():
    N, X = (int(i) for i in input().split())
    L = [int(i) for i in input().split()]
    from itertools import accumulate
    S = list(accumulate([0] + L))
    ans = 0
    for s in S:
        if X < s:
            break
        ans += 1
    print(ans)


if __name__ == '__main__':
    main()
