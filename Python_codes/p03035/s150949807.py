line = input()
numbers = [int(n) for n in line.split()]
if numbers[0] <= 5:
    predicted_value = 0
elif numbers[0] <= 12:
    predicted_value = numbers[1]//2
else:
    predicted_value = numbers[1]
print(predicted_value)