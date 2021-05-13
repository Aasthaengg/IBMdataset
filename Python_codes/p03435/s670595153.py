y1_list = list(map(int,input().split()))
y2_list = list(map(int,input().split()))
y3_list = list(map(int,input().split()))
L = [y1_list,y2_list,y3_list]
 
a1 = list()
a2 = list()
b1 = list()
b2 = list()
 
for i in range(3):
    a1.append(y1_list[i] - y2_list[i])
    a2.append(y2_list[i] - y3_list[i])
    b1.append(L[i][0] - L[i][1])
    b2.append(L[i][1] - L[i][2])
 
 
if (a1[0] == a1[1] and a1[2] == a1[0])and(b1[0] == b1[1] and b1[2] == b1[0]):
    if (a2[0] == a2[1] and a2[2] == a2[0])and(b2[0] == b2[1] and b2[2] == b2[0]):
        print("Yes")
        
    else:
        print("No")
else:
    print("No")