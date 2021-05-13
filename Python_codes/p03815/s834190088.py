x = int(input())
count = 0

count = x//11*2
if 0 < x-count*11/2 <= 6:
    count += 1
elif 0 < x-count*11/2:
    count += 2
print(count)