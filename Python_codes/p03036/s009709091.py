def actual(r, D, x_2000):
    x_list = []
    x_n = x_2000

    for _ in range(1, 10 + 1):
        x_next = r * x_n - D
        x_n = x_next

        x_list.append(x_next)

    return '\n'.join([str(x) for x in x_list])

r, D, x_2000 = map(int, input().split())
print(actual(r, D, x_2000))