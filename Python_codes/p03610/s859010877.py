s = input()
ans = []
for i in range(len(s)):
    if i % 2 == 0:
        ans.append(s[i])
a = map(str, ans)
print(''.join(a))