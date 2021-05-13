r, D, x = map(int, input().split())
x_li = [x]
for i in range(1,11):
    next_x = x_li[i-1] * r - D
    x_li.append(next_x)
    print(next_x)