k = int(input())
count = 0

for i in range(k):
    if i % 2 == 0:
        for j in range(k):
            if j % 2 != 0:
                count += 1
print(count)