s = input()
n = len(s)
k = 'keyence'
a = 0
b = 6

for i in range(n):
    if k[a] == s[i]:
        a += 1
    else:
        break
    if a == 7:
        break

for i in range(n)[::-1]:
    if k[b] == s[i]:
        b -= 1
    else:
        break
    if b == -1:
        break
    
b = 7 - b - 1
if a + b >= 7:
    print('YES')
else:
    print('NO')