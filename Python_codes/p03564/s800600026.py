from itertools import product

n = int(input())
k = int(input())

li = [0,1]

lin = list(product(li, repeat=n))
mi = 10**18

for i in lin:
    point = 1
    for j in i:
        if j == 0:
            point *= 2
        else:
            point += k
    mi = min(point,mi)

print(mi)