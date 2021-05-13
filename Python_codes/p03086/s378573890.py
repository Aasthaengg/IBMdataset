S = input()

ACGT = ['A', 'C', 'G', 'T']

count = 0
max_count = 0
for s in S:
    if s in ACGT:
        count += 1
    else:
        max_count = max(max_count, count)
        count = 0
max_count = max(max_count, count)
print(max_count)