s = input()
s_r = list(reversed(s))
s = s[:len(s)//2]
s_r = s_r[:len(s_r)//2]

count = 0
for i in range(len(s)):
    if s[i] != s_r[i]:
        count += 1

print(count)
