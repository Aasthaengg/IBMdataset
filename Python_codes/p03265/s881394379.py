x1, y1, x2, y2 = map(int, input().split())
x2x1 = x2 - x1
y2y1 = y2 - y1    
v = x2x1 + y2y1 * 1j
turn90 = 0 + 1j
for _ in range(2):
    v = v * turn90
    x2 += int(v.real)
    y2 += int(v.imag)
    print(x2, y2, end=' ')