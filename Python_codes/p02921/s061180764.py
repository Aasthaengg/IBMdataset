forecast = input()
actual = input()
correct = 0

for i in range(len(forecast)):
    if forecast[i] == actual[i]:
        correct = correct + 1
print(correct)
