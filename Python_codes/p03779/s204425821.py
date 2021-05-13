x = int(input())

distance = 0
count = 0

i = 1
while distance < x:
    distance += i
    count += 1
    i += 1

print(count)