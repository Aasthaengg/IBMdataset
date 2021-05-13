n = int(input())
count = 0
for k in range(26):
    for d in range(14):
        if 4*k + 7*d == n:
            count += 1
print('Yes' if count >= 1 else 'No')