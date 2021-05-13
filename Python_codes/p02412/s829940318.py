array = []
while 1 :
    n = input()
    if n == "0 0":
        break
    array.append(n.split())
for i in range(len(array)):
    count = 0
    for i2 in range(1,int(array[i][0])+1):
        for i3 in range(i2+1,int(array[i][0])+1):
            number =int(array[i][1])-(i2+i3)
            if number > i3 and number <= int(array[i][0]):
                count += 1
    print(count)