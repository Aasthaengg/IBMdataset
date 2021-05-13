s = input()

n = len(s)

a = 0
b = 0
c = 0

for i in range(n):
    if s[i] == 'a':
        a += 1
    elif s[i] == 'b':
        b += 1
    else:
        c += 1
min_num = min(a,b,c)
a -= min_num
b -= min_num
c -= min_num

if a <= 1 and b <= 1 and c <= 1:
    print('YES')
else:
    print('NO')