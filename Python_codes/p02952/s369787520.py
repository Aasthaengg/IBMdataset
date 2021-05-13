n = int(input())

count = 0
for num in range(1, n+1):
    if len(str(num)) % 2 != 0:
        count += 1
print(count)