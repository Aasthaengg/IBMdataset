s = input()
t = 'AKIHABARA'
if len(s) > len(t):
    print('NO')
    exit()
s += (len(t) - len(s)) * '#'
j = 0
for i in range(len(t)):
    if s[j] == t[i]:
        j += 1
    elif not (s[j] != 'A' and t[i] == 'A'):
        print('NO')
        exit()
print('YES')