c_list=[]
for i in range(3):
    c_list.append([int(i) for i in input().split()])
#print(c_list)

#c11
c_11=c_list[0][0]
ans=0
for a_1 in range(c_11+1):
    b_1=c_11-a_1
    b_2=c_list[0][1]-a_1
    b_3=c_list[0][2]-a_1
    if c_list[1][0]-b_1==c_list[1][1]-b_2==c_list[1][2]-b_3 and c_list[2][0]-b_1==c_list[2][1]-b_2==c_list[2][2]-b_3:
        print("Yes")
        ans=1
        exit()

if ans==0:
    print("No")