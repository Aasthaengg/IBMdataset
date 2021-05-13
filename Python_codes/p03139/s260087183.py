n, a, b = map(int,input().split())
h = min(a, b)
c = a+b-n
if c < 0:
    l = 0
else:
    l = c
print(h, l)