times, first, first_amount, second_amount = [int(input()) for i in range(4)]
total = 0
for i in range(times):
    if first > 0:
        total += first_amount
        first -= 1
    else:
        total += second_amount
print(total)
