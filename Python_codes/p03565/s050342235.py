s = input()
t = input()
n, m = len(s), len(t)

for i in range(n - m, -1, -1):
    match = True
    for j in range(m):
        if s[i + j] == '?' or s[i + j] == t[j]:
            continue
        else:
            match = False
            break

    if match:
        ans = ""
        for j in range(i):
            if s[j] == '?':
                ans += 'a'
            else:
                ans += s[j]
        ans += t
        for j in range(i + m, n):
            if s[j] == '?':
                ans += 'a'
            else:
                ans += s[j]
        print(ans)
        exit()
print("UNRESTORABLE")
