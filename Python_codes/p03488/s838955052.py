S = input()
x, y = map(int, input().split())

mem_x = []
mem_y = []
is_x = True
c = 0
S += 'T'
for s in S:
    if s == 'T':
        if is_x:
            if len(mem_x) == 0 or c != 0:
                mem_x.append(c)
            c = 0
        else:
            if c != 0:
                mem_y.append(c)
            c = 0
        is_x = not is_x
    else:
        c += 1

x = abs(x - mem_x.pop(0)) if len(mem_x) > 0 else abs(x)
y = abs(y)

for i in sorted(mem_x, reverse=True):
    x = abs(x-i)
for j in sorted(mem_y, reverse=True):
    y = abs(y-j)

if x == y == 0:
    print('Yes')
else:
    print('No')
