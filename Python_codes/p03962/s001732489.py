num = [0] * 100
for i in map(int, input().split()):
    num[i-1] += 1

count = 0
for i in num:
    if i >= 1:
        count += 1

print(count)