N = input()

count = 0

for i in range(10):
    if str(i)*3 in N:
        count += 1

print('Yes' if count else 'No')