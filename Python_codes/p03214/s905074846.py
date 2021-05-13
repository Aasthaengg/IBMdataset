n = int(input())
a = [int(s) for s in input().split()]
avg = sum(a) / len(a)

min_abs = 100
index = 0
for i in range(len(a)):
    if abs(avg - a[i]) < min_abs:
        min_abs = abs(avg - a[i])
        index = i
print(index)