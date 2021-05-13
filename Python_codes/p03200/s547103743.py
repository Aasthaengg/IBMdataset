S = input()

b_count = 0
result = 0
for i in S:
    if i == 'B':
        b_count += 1
        w_count = 0
    else:
        if b_count != 0:
            result += b_count

print(result)