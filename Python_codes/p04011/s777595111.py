list1 = []
for i in range(4):
    list1.append(int(input()))
if list1[0] >= list1[1]:
    print(list1[1] * list1[2] + (list1[0] - list1[1]) * list1[3])
else:
    print(list1[0] * list1[2])