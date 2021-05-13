s = input()
s1 = s.replace('x', '')

if s1 != s1[::-1]:
    print(-1)
else:
    li = [0] * (len(s1) + 1)
    cnt = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 'x':
            li[cnt] += 1
        else:
            cnt += 1

    for i in range((len(s1)+1) // 2):
        a = li[i]
        b = li[-i-1]
        ans += abs(a-b)

    print(ans)
