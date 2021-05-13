number = [int(x) for x in input().split()]
#S
#1 -> 2
#2 -> 6
#3 -> 3
#4 -> 4
#5 -> 1
#6 -> 5
order = input()

for i in range(len(order)):
    number_2 = [number[i] for i in range(len(number))]
    if order[i] == 'S':
        number[0] = number_2[4]
        number[1] = number_2[0]
        number[4] = number_2[5]
        number[5] = number_2[1]
    if order[i] == 'W':
        number[0] = number_2[2]
        number[2] = number_2[5]
        number[3] = number_2[0]
        number[5] = number_2[3]
    if order[i] == 'E':
        number[0] = number_2[3]
        number[2] = number_2[0]
        number[3] = number_2[5]
        number[5] = number_2[2]
    if order[i] == 'N':
        number[0] = number_2[1]
        number[1] = number_2[5]
        number[4] = number_2[0]
        number[5] = number_2[4]
    #print(number)

print(number[0])