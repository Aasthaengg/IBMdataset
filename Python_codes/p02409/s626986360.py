house = {1:[[0 for i in range(10)] for j in range(3)], 2:[[0 for i in range(10)] for j in range(3)],
         3:[[0 for i in range(10)] for j in range(3)], 4:[[0 for i in range(10)] for j in range(3)]}
n = int(input())
for i in range(n):
    building, floor, room, people_numbers = [int(j) for j in input().split()]
    house[building][floor - 1][room - 1] += people_numbers

partition = "#"*20
for i in range(4):
    for j in range(3):
        tmp_list = [str(tmp) for tmp in house[i + 1][j]]
        print(" {}".format(" ".join(tmp_list)))
        if j == 2 and i != 3: print(partition)