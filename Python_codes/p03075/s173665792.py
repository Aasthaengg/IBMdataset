min_x = 123
max_x = 0

for _ in range(5):
    x = int(input())
    if x <= min_x:
        min_x = x
    if x >= max_x:
        max_x = x

k = int(input())
if k < max_x-min_x:
    print(":(")
else:
    print("Yay!")