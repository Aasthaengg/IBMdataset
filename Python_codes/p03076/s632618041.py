import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

food = []

for _ in range(5):
    food.append(inint())

all = sum(food)
loss = []

for f in food:
    loss_t = 200
    for i in range(0,131, 10):
        if 0 <= i-f < loss_t:
            loss_t = abs(f-i)
    loss.append(loss_t)

print(all+sum(loss)-max(loss))