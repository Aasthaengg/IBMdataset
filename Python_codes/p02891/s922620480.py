s = list(input())
n = int(input())
ans = 0
if s[0] != s[-1]:
    cnt = 1
    tmp = ''
    for i in range(len(s)):
        if i == 0:
            tmp = s[i]
            continue
        if tmp == s[i]:
            cnt += 1
        else:
            ans += cnt // 2
            cnt = 1
            tmp = s[i]
    ans += cnt // 2
    print(ans*n)
else:
    cnt = 1
    tmp = ''
    f = 0
    for i in range(len(s)):
        if i == 0:
            tmp = s[i]
            continue
        if tmp == s[i]:
            cnt += 1
        else:
            if f == 0:
                f = cnt
            ans += cnt // 2
            cnt = 1
            tmp = s[i]
    ans += cnt // 2
    if f == 0:
        print((cnt*n)//2)
    else:
        m = ans - f//2 - cnt//2
        ans = f // 2 + cnt // 2
        # print(m,ans)
        ans += m * n
        # print(m*n)

        ans += (n-1) * ((f+cnt) // 2)
        # print((n-1)*((f+cnt)//2))
        print(ans)
