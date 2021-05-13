habitant_dictionary = {}
for building in range(1, 4 + 1):
    habitant_dictionary[building] = [0] * 30

information_number = int(raw_input())
while 0 < information_number:
    data = [int(x) for x in raw_input().split()]
    habitant_dictionary[data[0]][(int(data[1]) - 1) * 10 + (int(data[2]) - 1)] += int(data[3])
    information_number -= 1

for building in range(1, 4 + 1):
    for i in range(0, 30, 10):
        print(' ' + ' '.join([str(x) for x in habitant_dictionary[building][i:i + 10]]))
    if building is not 4:
        print('#' * 20)