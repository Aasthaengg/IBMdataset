from collections import deque

S = input()

d = deque(S)


left = 0
right = len(d) - 1

count = 0
while left < right:
    #print(f'{left=}, {right=}')
    if d[right] == d[left]:
        left += 1
        right -= 1
    else:
        if d[right] == 'x':
            count += 1
            right -= 1
        elif d[left] == 'x':
            count += 1
            left += 1
        else:
            count = -1
            print(-1)
            break

if count != -1:
    print(count)
