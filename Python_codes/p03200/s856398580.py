s = input()
s = s[::-1]

cnt = 0
b = -1

for idx in range(len(s)):
    if s[idx] is 'W':
        continue
    b += 1
    cnt = cnt + idx - b

print(cnt)