array = []

for i in range(3):
    val = input().split()
    array.append(val)

A,B = [int(s) for s in array[1]]

if array[2][0] == array[0][0]:
    print(str(A - 1) + " " + str(B))
else:
    print(str(A) + " " + str(B - 1))
