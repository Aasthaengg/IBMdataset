a, b, c = (int(n) for n in input().split())
if c > (a - b): print(c - (a - b))
else: print('0')