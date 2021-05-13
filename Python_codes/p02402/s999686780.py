n = int(input())
data = list(map(int, input().split()))

min = data[0]
max = data[0]
sum = 0
for x in data:
    sum += x
    if x > max:
        max = x
    if x < min:
        min = x

print("%d %d %d" % (min, max, sum))