s = int(input())

numbers = []

for i in range(10000001):
    if i == 0:
        numbers.append(s)
    else:
        if numbers[-1] % 2 == 0:
            numbers.append(numbers[-1] // 2)
        else:
            numbers.append(3*numbers[-1]+1)
    if numbers.count(4) == 2 or numbers.count(2) ==2 or numbers.count(1) == 2:
        break

print(len(numbers))