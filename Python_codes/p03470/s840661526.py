n = int(input())
d = [0] * 101
for i in range(0, n):
    inp = int(input())
    d[inp] += 1

count = 0
for i in d:
    if i > 0:
        count += 1
print(count)