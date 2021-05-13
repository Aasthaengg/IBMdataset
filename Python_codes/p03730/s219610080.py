s = input().split()

a = int(s[0])
b = int(s[1])
c = int(s[2])

check = False

for i in range(b):
    p = a * i
    if p % b == c:
        check = True
        break

if check:
    print('YES')
else:
    print('NO')
