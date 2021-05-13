s = input()
s_r = list(reversed(s))
count = 0

for i in range(len(s)):
    if s[i] != s_r[i]:
        count += 1

print(count//2)