n = int(input())
count = 0
for i in range(n):
    if len(str(i + 1)) % 2 == 1:
        count += 1
print(count)