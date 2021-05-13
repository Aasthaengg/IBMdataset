s = input()
if len(s) % 2 == 0:
    s_1 = s[:len(s) // 2]
    s_2 = s[len(s) // 2:][::-1]
else:
    s_1 = s[:len(s) // 2 + 1]
    s_2 = s[len(s) // 2:][::-1]
ans = 0
for i in range(len(s_1)):
    if s_1[i] != s_2[i]:
        ans += 1
print(ans)