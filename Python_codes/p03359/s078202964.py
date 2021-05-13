a, b = list(map(int, input().split()))
count = 0
m = [i for i in range(1, a)]
for month in m:
    count += 1
if b >= a:
    count += 1
print(count)
