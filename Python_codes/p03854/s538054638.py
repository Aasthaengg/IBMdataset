import sys
sys.setrecursionlimit(10000)

s = 'HAKUTYUMU' + input()


while s != 'HAKUTYUMU':
    next_s = s

    if s[-5:] == 'dream':
        next_s = s[:-5]
    if s[-7:] == 'dreamer':
        next_s = s[:-7]
    if s[-5:] == 'erase':
        next_s = s[:-5]
    if s[-6:] == 'eraser':
        next_s = s[:-6]

    if s == next_s:
        print('NO')
        exit()

    s = next_s

print('YES')
