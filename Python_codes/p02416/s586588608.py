values = []
while True:
    value = input()
    if value == "0":
        break
    else:
        values.append(value)

for value in values:
    summation = 0
    for i in range(len(value)):
        summation += int(value[i])
    print(summation)

