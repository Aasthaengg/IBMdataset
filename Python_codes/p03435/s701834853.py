l = list(list(map(int,input().split())) for i in range(3))
first = l[0][0]-l[0][1]
second = l[0][1]-l[0][2]
first1 = l[0][0]-l[1][0]
second2 = l[1][0]-l[2][0]

for k in range(3):
    if (l[k][0]-l[k][1] != first or l[k][1]-l[k][2] != second):
        print("No")
        exit()
for j in range(3):
    if (l[0][k]-l[1][k] != first1  or l[1][k]-l[2][k] != second2):
        print("No")
        exit()     
print("Yes")
