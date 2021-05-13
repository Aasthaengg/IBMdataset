a, b = map(int, input().split(" "))
sum = a + b
avg = sum / 2
if sum % 2 == 1:
    avg += 1

print(int(avg))