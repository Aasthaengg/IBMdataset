def codefes16qa_c():
    s = str(input())
    k = int(input())
    n = len(s)
    ans = ''
    for i in range(n):
        if s[i] == 'a':
            ans += s[i]
            continue
        step2a = 1 + ord('z') - ord(s[i])
        if step2a <= k:
            ans += 'a'
            k -= step2a
        else:
            ans += s[i]
    if k > 0:
        last = ord(ans[-1]) + (k % 26)
        ans = ans[:n-1] + chr(last)
    print(ans)

codefes16qa_c()