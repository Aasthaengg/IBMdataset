A_element = []
B_element = []
C_element = []
ele_num = [int(x) for x in input().split()]
for i in range(ele_num[0]):
    C_element.append(0)
for i in range(ele_num[0]):
    element = [int(x) for x in input().split()]
    A_element.append(element)

for i in range(ele_num[1]):
    element = int(input())
    B_element.append(element)

for i in range(ele_num[0]):
    for j in range(ele_num[1]):
        C_element[i] =C_element[i] + (A_element[i][j] * B_element[j])

for out in C_element:
    print(out)

