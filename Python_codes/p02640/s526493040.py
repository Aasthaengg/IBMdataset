x, y = map(int, input().split())

crane_legs_tmp = 2*x
if crane_legs_tmp > y:
    print("No")
elif crane_legs_tmp == y:
    print("Yes")
else:
    flag = 0
    for i in range(x):
        if (x - (i+1))*2 + (i+1)*4 == y:
            flag = 1
            break
    if flag == 1:
        print("Yes")
    else :
        print("No")