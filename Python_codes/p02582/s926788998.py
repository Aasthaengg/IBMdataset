s = input()
max_count = 0
count = 0
for i in s:
    if i == "R":
        count += 1
    else:
        max_count = max(max_count, count)
        count = 0
max_count = max(max_count, count)
print(max_count)