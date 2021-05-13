S = input()

max_num = 0

count = 0
for x in S:
    if x in 'ACGT':
        count += 1
    else:
        max_num = max(max_num, count)
        count = 0

print(max(max_num, count))