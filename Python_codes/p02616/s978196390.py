n, k = map(int, input().split())
a_list = list(map(int, input().split()))
mod = 10**9+7
a_list.sort()
ans = 1
if k % 2 == 1 and a_list[-1] < 0:
    for i in range(k):
        ans *= a_list[n - 1 - i]
        ans %= mod
else:
    l = 0
    r = -1
    mlt1 = a_list[0] * a_list[1]
    mlt2 = a_list[-2] * a_list[-1]
    count = 0
    while True:
        if count == k:
            break
        elif count == k - 1:
            ans *= a_list[r] % mod
            ans %= mod
            break
        if mlt1 >= mlt2:
            ans *= mlt1 % mod
            l += 2
            count += 2
            if l <= n - 2:
                mlt1 = a_list[l + 1] * a_list[l]
        else:
            ans *= a_list[r] % mod
            r -= 1
            count += 1
            if r >= - n + 1:
                mlt2 = a_list[r - 1] * a_list[r]
        ans %= mod
print(ans)