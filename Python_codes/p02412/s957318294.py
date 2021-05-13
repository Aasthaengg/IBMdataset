from itertools import combinations
original_vals = []
original_labels = []

while True:
    n, x = list(map(int, input().split()))
    if n+x == 0:
        break
    l = [ i for i in range(1,n+1)]
    original_vals.append(l)
    original_labels.append(x)

for i,row in enumerate(original_vals):
    cs = list(combinations(row, 3))
    count = 0
    for c in cs:
        if sum(c) == original_labels[i]:
            count += 1
    print(count)