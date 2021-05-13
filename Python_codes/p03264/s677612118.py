count = 0
k = int(input())
for i in range(1, k + 1):
    for j in range(i + 1, k + 1, 2):
        count += 1
print(count)