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

 
 
if (a1[0] == a1[1] and a1[2] == a1[0]):
    if (a2[0] == a2[1] and a2[2] == a2[0]):
        print("Yes")
        
    else:
        print("No")
else:
    print("No")