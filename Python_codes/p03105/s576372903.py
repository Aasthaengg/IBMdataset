line = input()
numbers = [int(n) for n in line.split()]
predicted_value = min(numbers[1]//numbers[0], numbers[2])
print(predicted_value)