
line = [int(i) for i in input().split(" ")]
b = line[0]
flag = 0
for i in line:
    if i != b:
        flag = 1
if flag == 1:
    print("No")
else:
    print("Yes")