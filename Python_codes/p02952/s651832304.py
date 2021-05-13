n = int(input())
count = 0
if n >= 10:
    count += 9
    if n >= 1000:
        count += 900
        if n == 100000:
            count += 90000
        elif n >= 10000:
            count += n - 10000 + 1
    elif n >= 100:
        count += n - 100 + 1
else:
    count += n
print(count)