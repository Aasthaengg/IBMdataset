s = input()
n = int(s)

lucas = [2, 1]

x = 0

index = 0

while (index < n):
    x = lucas[index] + lucas[index + 1]
    lucas.append(x)
    index += 1

print(lucas[index])