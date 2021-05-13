data = list(map(int, input().split()))
order = list(input())

up = 1
front = 2
right = 3

move = "NSEW"

for m in order:
    i = move.index(m)
    if i == 0:
        up, front = front, 7 - up
    elif i == 1:
        up, front = 7 - front, up
    elif i == 2:
        up, right = 7 - right, up
    else:
        up, right = right, 7 - up

print(data[up - 1])