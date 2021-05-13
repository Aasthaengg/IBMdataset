#!/usr/bin/env python

n = int(input())
a = list(map(int, input().split()))
d = [0 for _ in range(n-1)]
for i in range(n-1):
    d[i] = a[i+1]-a[i]

# print(d)
ans = 1 
state = 'flat'
for i in range(n-1):
    if i == 0:
        if d[i] > 0:
            state = 'up'    
        elif d[i] < 0:
            state = 'down'

    else:
        if d[i] > 0:
            if state == 'flat':
                state = 'up'
            elif state == 'down':
                state = 'flat'
                ans += 1

        elif d[i] < 0:
            if state == 'flat':
                state = 'down'
            elif state == 'up':
                state = 'flat'
                ans += 1

print(ans)
