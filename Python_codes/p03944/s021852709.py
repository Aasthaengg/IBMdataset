s = input().split()

w = int(s[0])
h = int(s[1])
n = int(s[2])

max_x = w
max_y = h
min_x = 0
min_y = 0

x = []
y = []
a = []

for num in range(n):
    v = input().split()
    x.append(int(v[0]))
    y.append(int(v[1]))
    a.append(int(v[2]))

for num in range(n):
    if a[num] == 1:
        if x[num] > min_x:
            min_x = x[num]
    elif a[num] == 2:
        if x[num] < max_x:
            max_x = x[num]
    elif a[num] == 3:
        if y[num] > min_y:
            min_y = y[num]
    else:
        if y[num] < max_y:
            max_y = y[num]

y_length = max_y - min_y
if y_length < 0:
    y_length = 0
x_length = max_x - min_x
if x_length < 0:
    x_length = 0
answer = x_length * y_length

print(answer)
        


