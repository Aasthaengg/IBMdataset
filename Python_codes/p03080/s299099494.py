n = int(input())
s = input()
r = 0
b=0
for i in range(n):
    if s[i] == 'R':
        r += 1
    else:
        b += 1
if b < r:
    print('Yes')
else:
    print('No')