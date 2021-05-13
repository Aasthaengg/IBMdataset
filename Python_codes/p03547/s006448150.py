x, y = map(str, input().split())
s = ['A', 'B', 'C', 'D', 'E', 'F']
for i in range(6):
    if x == s[i]:
        xi = i
    if y == s[i]:
        yi = i
if xi > yi:
    print('>')
elif xi < yi:
    print('<')
else:
    print('=')