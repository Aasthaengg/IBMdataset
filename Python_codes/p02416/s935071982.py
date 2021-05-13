values = []
while True:
    val = int(input())
    if 0 == val:
        break
    values.append(val)

for val in values:
    sum = 0
    while val >= 1:
        sum += (val % 10)
        val //= 10
    print(sum)