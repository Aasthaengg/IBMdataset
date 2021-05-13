input()
A = map(int, input().split())
one, two, four = 0,0,0

for a in A:
    if a % 4 == 0:
        four += 1
    elif a % 2 == 0:
        two += 1
    else:
        one += 1

if one <= four or (one == four + 1 and two == 0):
    print('Yes')
else:
    print('No')
