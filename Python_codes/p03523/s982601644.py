s = input()
b = 'AKIHABARA'
n = len(b)
if  n < len(s):
    print('NO')
    exit()
j = 0
s += 'A'
for i in range(n):
    if b[i] == 'A' and s[j] == 'A':
        j += 1
    elif b[i] == 'A' and s[j] != 'A':
        continue
    elif b[i] == s[j]:
        j += 1
    else:
        print('NO')
        exit()
print('YES')
    
