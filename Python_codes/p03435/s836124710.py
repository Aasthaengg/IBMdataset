lis = []
for _ in range(3):
    lis.append(list(map(int, input().split())))

flag1 = 0
flag2 = 0
for a1 in range(101):
    b1 = lis[0][0] - a1
    b2 = lis[0][1] - a1
    b3 = lis[0][2] - a1
    
    for a2 in range(101):
        if a2 + b1 == lis[1][0] and a2 + b2 == lis[1][1] and a2 + b3 == lis[1][2]:
            flag1 = 1
            break
        else:
            flag1 = 0
            
    for a3 in range(101):
        if a3 + b1 == lis[2][0] and a3 + b2 == lis[2][1] and a3 + b3 == lis[2][2]:
            flag2 = 1
            break
        else:
            flag2 = 0
            
    if flag1 == 1 and flag2 ==1:
        print("Yes")
        exit()

print("No")