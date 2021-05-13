r, c = map(int, input().split())
last = [0]*(c+1)
for i in range(r):
    columns = list(map(int, input().split()))
    for j in range(c):
        last[j] += columns[j]
    total = sum(columns)
    last[c] += total
    columns.append(total)
    print(' '.join(map(str, columns)))
print(' '.join(map(str,last)))
