n = int(input())

a = map(int, input().split(" "))

sorted = sorted(a)

sum = 0
prev = -1
for p in sorted:
    if prev >= 0:
        sum += p - prev

    prev = p

print(sum)

