s = input()

k = 'keyence'

for i in range(len(s)):
    for j in range(i, len(s)):
        t = s[:i] + s[j:]
        if k == t:
            print('YES')
            exit()

print('NO')

