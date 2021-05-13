N = int(input())
D = []
count, temp = 0, 0

for n in range(N):
    input_line = input().split()
    if (int(input_line[0]) == int(input_line[1])):
        count += 1
        if count == 3:
            temp = 1
    elif(temp ==1):
        break
    else:
        count = 0

if count >= 3:
        print('Yes')

else:
        print('No')