R, C = map(int, raw_input().split())
chart = [map(int, raw_input().split()) for r in range(R)]
col = [0] * C
for r in range(R):
    row = chart[r]
    row.append(sum(row))
    print ' '.join(map(str, row))
    for c in range(C):
        col[c] += row[c]
for c in range(C):
    print col[c],
print sum(col)