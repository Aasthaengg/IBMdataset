h, w, k = map(int, input().split())

r_n = [0] * h
c_n = [0] * w
bomb_table = set()
for i in range(k):
    hi, wi = map(int, input().split())
    hi -= 1
    wi -= 1
    r_n[hi] += 1
    c_n[wi] += 1
    bomb_table.add((hi, wi))

max_x = max(c_n)
max_y = max(r_n)
ans = max_x + max_y

max_x_table = set()
max_y_table = set()

for i in range(h):
    if r_n[i] == max_y:
        max_y_table.add(i)

for i in range(w):
    if c_n[i] == max_x:
        max_x_table.add(i)

for i in max_y_table:
    for j in max_x_table:
        if (i, j) not in bomb_table:
            print(ans)
            exit(0)
print(ans - 1)
