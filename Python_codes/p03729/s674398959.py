list = [i for i in input().split(" ")]
loop = 0
char = list[0][0]
for i in list:
    if char == i[0]:
        char = i[len(list[loop]) - 1]
        loop = loop + 1
    else:
        print("NO")
        exit()
print("YES")
