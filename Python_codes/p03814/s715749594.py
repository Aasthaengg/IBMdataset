s = input()
l = -1
r = 0
for i, si in enumerate(s):
    if si == 'Z':
        r = i
    elif si == 'A' and l == -1:
        l = i
print(r-l+1)