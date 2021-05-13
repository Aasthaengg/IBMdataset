s = input()
n = len(s)
k = int(input())

if len(set(s)) == 1:
    print(n * k // 2)

else:
    memo = []
    tmp = 1
    for i in range(n-1):
        if s[i] == s[i+1]:
            tmp += 1
        else:
            memo.append(tmp)
            tmp = 1
    memo.append(tmp)
    m = len(memo)

    if s[0] == s[-1]:
        ans = 0
        for i in range(m):
            if i == 0 or i == m-1:
                ans += memo[i] // 2
            else:
                ans += (memo[i] // 2) * k
        ans += ((memo[0] + memo[-1]) // 2) * (k-1)

    else:
        ans = sum(memo[i] // 2 for i in range(m)) * k

    print(ans)