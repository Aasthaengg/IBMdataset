from itertools import product

h, w, k = map(int, input().split())
AL = []
count = 0
for i in range(h):
    c = list(input())
    AL.append(c)
for a in product(range(2), repeat=h):
    for b in product(range(2), repeat=w):
        black = 0
        for i in range(h):
            for j in range(w):
                if AL[i][j] == "#" and (a[i] and b[j]):
                    black += 1
        if k == black:
            count += 1
print(count)