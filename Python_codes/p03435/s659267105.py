data=[]
for i in range(3):
    data.append(list(map(int,input().split())))
if data[0][0]-data[1][0] == data[0][1]-data[1][1] == data[0][2]-data[1][2]:
    if data[1][0]-data[2][0] == data[1][1]-data[2][1] == data[1][2]-data[2][2]:
        if data[0][0]-data[0][1] == data[1][0]-data[1][1] == data[2][0]-data[2][1]:
            if data[0][1]-data[0][2] == data[1][1]-data[1][2] == data[2][1]-data[2][2]:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")