N = int(input())
counter = 0
for i in range(1, N + 1):
    if len(str(i)) % 2:
        counter += 1
print(counter)
