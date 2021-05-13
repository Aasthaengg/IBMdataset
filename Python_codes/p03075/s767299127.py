antennas = [
    int(input()),
    int(input()),
    int(input()),
    int(input()),
    int(input())
]
k = int(input())

message = 'Yay!'
for i in range(0, 5 - 1):
    if message == ':(':
        break
    for j in range(i + 1, 5):
        if (antennas[j] - antennas[i]) > k:
            message = ':('
            break
print(message)