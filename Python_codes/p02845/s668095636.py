def main():
    MOD = 10**9 + 7
    N = int(input())
    A = list(map(int, input().split()))
    hat_cnt = [0, 0, 0]
    ans = 1
    for a in A:
        t = len([c for c in hat_cnt if c == a])
        if t == 0:
            ans = 0
            break
        ans *= t
        ans %= MOD
        for i in range(len(hat_cnt)):
            if hat_cnt[i] == a:
                hat_cnt[i] += 1
                break
    print(ans)


if __name__ == '__main__':
    main()