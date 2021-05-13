s = input()
compress = []
i = 0
while i < len(s):
    if s[i:i+2] == 'BC':
        compress.append('D')
        i += 2
    else:
        compress.append(s[i])
        i += 1
ans = 0
count = 0
for x in compress:
    if x == 'A':
        count += 1
    elif x == 'D':
        ans += count
    else:
        count = 0
print(ans)