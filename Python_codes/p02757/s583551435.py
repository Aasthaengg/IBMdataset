def main():
    N, P = (int(i) for i in input().split())
    S = input()
    ans = 0
    if P == 2 or P == 5:
        for i, s in enumerate(S, start=1):
            if int(s) % P == 0:
                ans += i
        return print(ans)
    cnt = [0]*P
    cnt[0] += 1
    d = 1
    cur = 0
    for s in S[::-1]:
        s = int(s)
        cur += (s * d) % P
        cur %= P
        d *= 10
        d %= P
        cnt[cur] += 1
    for c in cnt:
        if c:
            ans += c*(c-1)//2
    print(ans)


if __name__ == '__main__':
    main()
