rate, D, x_2000 = map(int, input().split())
current_x = x_2000

for i in range(10):
    next_x = rate * current_x - D
    print(next_x)
    current_x = next_x
