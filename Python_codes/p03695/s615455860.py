#!/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))

def rank(n):
    if 1 <= n <= 399:
        return 'gray'
    elif 400 <= n <= 799:
        return 'brown'
    elif 800 <= n <= 1199:
        return 'green'
    elif 1200 <= n <= 1599:
        return 'skyblue'
    elif 1600 <= n <= 1999:
        return 'blue'
    elif 2000 <= n <= 2399:
        return 'yellow'
    elif 2400 <= n <= 2799:
        return 'orange'
    elif 2800 <= n <= 3199:
        return 'red'
    else:
        return 'others'

colors = [rank(a[i]) for i in range(n)]
numother = colors.count('others')
colors = set(colors)

if 'others' in colors:
    colors.remove('others')
    minimum = len(colors)
    tmp = minimum
    if minimum == 0:
        minimum = 1 
    maximum = tmp + numother
else:
    minimum = len(colors)
    maximum = minimum

print(minimum, maximum)
