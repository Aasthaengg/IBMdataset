s = input()
cnt = 0
for s1, s2 in zip(s, s[::-1]):
    if s1 != s2:
        cnt += 1
print(cnt // 2)