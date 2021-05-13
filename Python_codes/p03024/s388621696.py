s = input()
count = 0
for a in range(len(s)):
    if(s[a] == 'x'):
        count += 1

if(count >= 8):
    print('NO')
else:
    print('YES')