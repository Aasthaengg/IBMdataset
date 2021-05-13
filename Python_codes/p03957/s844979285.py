s = input()
n = 0
m = 0
for i in range(0, len(s)):
    if s[i] == 'C':
        n = 1
        break
for j in range (i, len(s)):
    if s[j] == 'F':
        m = 1
        break
if n == 1 and m == 1:
    print('Yes')
else:
    print('No')