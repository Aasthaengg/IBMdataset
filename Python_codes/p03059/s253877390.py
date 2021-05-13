line = input()
numbers = [int(n) for n in line.split()]
time = numbers[2]*10 + 5
biscuits = numbers[1]
time_taken = numbers[0] * 10
predicted_value = 0
while time >= 0:
    if time - time_taken >= 0:
        predicted_value += biscuits
    time -= time_taken
print(predicted_value)