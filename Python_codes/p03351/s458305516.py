data = input()
data1,data2,data3,data4 = data.split()
data1 = int(data1)
data2 = int(data2)
data3 = int(data3)
data4 = int(data4)


if abs(data1 - data3) <= data4:
    print('Yes')
elif abs(data1 - data2) <= data4 and abs(data2 - data3) <= data4:
    print('Yes')
else:
    print('No')