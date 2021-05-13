n,p = map(int, input().split())
s = input()

if p == 2 or p == 5:
    ans = 0
    for i in range(n):
        if int(s[i]) % p == 0:
            ans += i + 1
    print(ans)



else:
    res = 0
    cnt = [0] * p
    for i in range(n):
        res = (res + int(s[n-1-i]) * pow(10, i, p)) % p
        cnt[res] += 1

    ans = 0
    for c in cnt:
        ans += c * (c-1) // 2
    ans += cnt[0]
    print(ans)