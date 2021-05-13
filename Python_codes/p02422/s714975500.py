str = list(input())
q = int(input())

temp = []
for i in range(q):
    comm = input().split()

    if comm[0] == "replace":
        temp = list(comm[3])
        for i in range(0,int(comm[2])-int(comm[1])+1):
            str[int(comm[1])+i]=temp[i]
        temp.clear()
    elif comm[0] == "reverse":
        for i in reversed(range(int(comm[1]), int(comm[2])+1)):
            temp.append(str[i])
        for i in range(0, int(comm[2])-int(comm[1])+1):
            str[i+int(comm[1])] = temp[i]
        temp.clear()
    else:
        for i in range(int(comm[1]), int(comm[2])+1):
            temp.append(str[i])
        print(''.join(temp))
        temp.clear()
