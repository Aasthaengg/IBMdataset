n, k = map(int, input().split())
v = list(map(int, input().split()))

if k <= n:
    ans = - 10 ** 9
    for i in range(k + 1):
        for j in range(i + 1):
            tmp = v[:j]
            if i != j:
                tmp += v[-(i - j):]
            tmp.sort()
            ans = max(ans, sum(tmp[k - i:]))
            if k != i:
                ans = max(ans, sum(tmp[k - i - 1:]))

elif k >= 2 * n:
    v.sort(reverse = True)
    ans = 0
    for num in v:
        if num <= 0:
            break
        ans += num

else:
    ans = - 10 ** 9
    for i in range(n + 1):
        for j in range(i + 1):
            tmp = v[:j]
            if i != j:
                tmp += v[-(i - j):]
            tmp.sort(reverse = True)
            ans_tmp = 0
            for l, num in enumerate(tmp):
                if l >= 2 * i - k and num <= 0:
                    break
                ans_tmp += num
            ans = max(ans, ans_tmp)

print(ans)
