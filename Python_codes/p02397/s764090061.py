input_array=[]

while True:
    a, b = [int(x) for x in raw_input().split(" ")]

    if a == 0 and b == 0:
        break
    elif a > b:
        tmp = a
        a = b
        b = tmp

    input_num = str(a) + " " + str(b)
    input_array.append(input_num)

for x in range(0,len(input_array)):
    print(input_array[x])