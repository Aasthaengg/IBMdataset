grade=[]

while True:
    test_point=[]
    test_point=input().split()
    test_point[0]=int(test_point[0])
    test_point[1]=int(test_point[1])
    test_point[2]=int(test_point[2])
    if test_point[0]==-1 and test_point[1]==-1 and test_point[2]==-1:
        break
    elif test_point[0]==-1 or test_point[1]==-1:
        grade.append('F')
    elif test_point[0]+test_point[1]>=80:
        grade.append('A')
    elif test_point[0]+test_point[1]<80 and test_point[0]+test_point[1]>=65:
        grade.append('B')
    elif test_point[0]+test_point[1]<65 and test_point[0]+test_point[1]>=50:
        grade.append('C')
    elif test_point[0]+test_point[1]<50 and test_point[0]+test_point[1]>=30:
        if test_point[2]>=50:
            grade.append('C')
        else:
            grade.append('D')
    elif test_point[0]+test_point[1]<30:
        grade.append('F')

for i in range(0,len(grade)):
    print(grade[i])