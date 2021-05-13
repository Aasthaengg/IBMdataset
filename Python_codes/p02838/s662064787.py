def solve():
    MOD = 10**9 + 7

    N = int(input())
    As = list(map(int, input().split()))

    ans = 0
    for d in range(60):
        nums = [0, 0]
        for A in As:
            b = (A>>d) & 1
            nums[b] += 1
        v = nums[0]*nums[1]
        v *= pow(2, d, MOD)
        ans += v
        ans %= MOD

    print(ans)


solve()
