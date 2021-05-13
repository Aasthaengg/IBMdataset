n = int(input())
count = 0

for i in range(n):
    data = int(input())
    data = abs(data)
    if data == 2:
        count += 1
    elif pow(2,data-1,data) == 1:
            count += 1

print(count)