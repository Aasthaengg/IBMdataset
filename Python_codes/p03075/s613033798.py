antennas = [int(input()) for _ in range(5)]
k = int(input())

flag = True

for i in range(4):
    for j in range(i + 1, 5):
        if antennas[j] - antennas[i] > k:
            flag = False
            break

if flag:
    print('Yay!')
else:
    print(':(')