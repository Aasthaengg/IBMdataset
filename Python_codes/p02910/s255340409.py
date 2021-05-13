l = list(input())
f = False

for i in range(len(l)):
    if i % 2:
        if l[i] == 'L' or l[i] == 'U' or l[i] == 'D':
            f = True
        else:
            f = False
            break
    else:
        if l[i] == 'R' or l[i] == 'U' or l[i] == 'D':
            f = True
        else:
            f = False
            break

if f:
    print('Yes')
else:
    print('No')