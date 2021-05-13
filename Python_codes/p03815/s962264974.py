x = int(input())
count = 0
count = (x // 11)*2
if x % 11 == 0:
    count += 0
elif x % 11 <= 6:
    count += 1
else:
    count += 2
print(count)