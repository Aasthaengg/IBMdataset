S = input().split('T')
x, y = map(int, input().split())

x_axis = S[::2]
y_axis = S[1::2]

const = 8000
x_pos = 1 << const
y_pos = 1 << const
first = True
for s in x_axis:
    step = len(s)
    if first:
        x_pos <<= step
        first = False
    else:
        x_pos = x_pos << step | x_pos >> step

for s in y_axis:
    step = len(s)
    y_pos = y_pos << step | y_pos >> step

if x_pos >> (const+x) & 1 and y_pos >> (const+y) & 1:
    print('Yes')
else:
    print('No')