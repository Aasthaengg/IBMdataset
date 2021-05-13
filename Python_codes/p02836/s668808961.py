s = input()
l = len(s)
if l % 2 == 0:
    s_a = s[:l // 2]
    s_b = ''.join(list(reversed(s[l // 2:])))
else:
    s_a = s[:l // 2]
    s_b = ''.join(list(reversed(s[l // 2 + 1:])))

count = 0
for i in range(len(s_a)):
    if s_a[i] != s_b[i]:
        count += 1
print(count)