n = int(input())
counter = 0
for i in range(1, n+1, 2):
    divisor_counter = 0
    for j in range(1, i+1):
        if i % j == 0:
            divisor_counter += 1

    if divisor_counter == 8:
        counter += 1
print(counter)