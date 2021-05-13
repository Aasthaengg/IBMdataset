n = int(input())
s = input()

top_used = set()
used = set()
ans = 0
for i in range(n - 1):
    if int(s[i]) in top_used:
        continue
    top_used.add(int(s[i]))
    for j in range(i + 1, n):
        top = s[i] + s[j]
        if top not in used:
            ans += len(set(s[j + 1:]))
            used.add(top)


print(ans)
