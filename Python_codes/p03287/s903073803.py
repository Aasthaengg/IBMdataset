def main():
    N, M = (int(i) for i in input().split())
    A = [int(i) for i in input().split()]
    ans = 0
    s = [0] * (N + 1)
    for i in range(N):
        s[i+1] = (s[i] + A[i]) % M
    from collections import Counter
    c = Counter(s)
    for v in c.values():
        if v >= 2:
            ans += (v*(v-1))//2
    print(ans)


if __name__ == '__main__':
    main()
