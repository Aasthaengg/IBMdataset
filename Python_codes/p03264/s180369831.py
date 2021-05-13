k = int(input())
count = 0
for i in range(1, k):
    for j in range(i+1, k+1):
        if i % 2 == 1 and j % 2 == 0:
            count += 1
        elif i % 2 == 0 and j % 2 == 1:
            count += 1
print(count)