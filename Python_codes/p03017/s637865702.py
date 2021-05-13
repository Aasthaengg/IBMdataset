n, a, b, c, d = map(int, input().split())
s = list(input())
a -= 1
b -= 1
c -= 1
d -= 1
jump = True
if d < c:
    cnt = 0
    for i in range(b-1,d+2):
        if s[i] == '.':
            cnt += 1
        if cnt == 3:
            break
        if s[i] == '#':
            cnt = 0
    else:
        jump = False
cnt = 0
for i in range(a,c):
    if s[i] == '#':
        cnt += 1
    if s[i] == '.':
        cnt = 0
    if cnt == 2:
        jump = False
        break
for i in range(b,d):
    if s[i] == '#':
        cnt += 1
    if s[i] == '.':
        cnt = 0
    if cnt == 2:
        jump = False
        break
if jump:
    print('Yes')
else:
    print('No')