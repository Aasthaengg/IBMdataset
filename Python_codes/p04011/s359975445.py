n, k, x, y = (int(input()) for i in range(4))

total_payment = 0

for i in range(1, n + 1):
    if i <= k:
        total_payment += x
    else:
        total_payment += y

print(total_payment)