N = int(input())

s = 0
y = 0

for c in range(26):
    for d in range(15):
        s = c*4 + d*7
        if s == N:
            y += 1
            print('Yes')
            break
        else:
            pass
    if y > 0:
        break
    else:
        pass

if y == 0:
    print('No')
else:
    pass