(r, c) = [int(i) for i in input().split()]
last_row = [0 for _ in range(c+1)]

for _ in range(r):
    row = [int(i) for i in input().split()]
    for cc in range(c):
        last_row[cc] += int(row[cc])
        print(row[cc], end=' ')

    print(sum(row))

last_row[-1] = sum(last_row)
print(' '.join([str(a) for a in last_row]))