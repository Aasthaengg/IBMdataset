import sys
a, b, c, k = map(int, input().split())

if abs(b-a) >= 10**18: print('Unfair')
elif k%2 == 1: print(b-a)
else: print(a-b)
