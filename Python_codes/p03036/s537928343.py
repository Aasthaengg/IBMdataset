r, D, x_2000 = map(int, input().split())

x_2001 = r *x_2000 -D

memo = {2000: x_2000, 2001: x_2001}


def zen(n, x, r, D):
    x.append(r *x[n -1] -D)
    return x

x = []
x.append(x_2000)
for i in range(1, 11):
    print(zen(i, x, r, D)[-1])

