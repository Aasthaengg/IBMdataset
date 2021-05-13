s=input()
k='keyence'
if k in s:
    exit(print('YES'))

for i in range(len(k)):
    #print(s[:i], s[len(k)-i:])
    if s[:i]+s[len(s)-len(k)+i:] == k:
        exit(print('YES'))
print('NO')
