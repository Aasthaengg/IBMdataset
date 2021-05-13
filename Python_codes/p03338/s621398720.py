n = int(input())
s = input()

ans = 0
for i in range(len(s)):
    l = [s[j] for j in range(i + 1)]
    m = []
    for j in range(i + 1, len(s)):
        if s[j] in l and s[j] not in m:
            m.append(s[j])
    ans = max(ans, len(m))

print(ans)
