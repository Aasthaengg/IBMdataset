n = int(input())
s = input()
cnt = 0

for i in range(1, n):
    c = 0
    s1 = s[i:]
    s2 = s[:i]
    S = set(s1)

    for j in S:
        if j in s2:
            c += 1
    cnt = max(cnt, c)

print(cnt)