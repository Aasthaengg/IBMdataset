sum = 0
max = -10000000
min = 10000000

input()

for i in [int(x) for x in input().split()]:
    sum += i
    if i > max:
        max = i

    if i < min:
        min = i

print(min,max,sum)