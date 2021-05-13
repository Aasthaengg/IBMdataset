input_array = []

while True:
    input_num = int(raw_input())
    if input_num == 0:
        break
    input_array.append(input_num)

for x in range(0, len(input_array)):
    print("Case {}: " + str(input_array[x])).format(x+1)