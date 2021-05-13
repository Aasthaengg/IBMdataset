A, B, C = sorted(list(map(int, input().split())))
r = C-B
B += r
A += r
s = C-A
if s % 2 == 0:
    s = s//2
else:
    s = (s//2) + 2
print(r+s)
