s = list(input())
flag = True
for i,j in enumerate(s):
    if i % 2 == 0:
        if j == "R" or j =="U" or j == "D":
            flag = True
        else:
            flag = False
            break
    else:
        if j == "L" or j == "U" or j == "D":
            flag = True
        else:
            flag = False
            break
if flag == True:
    print("Yes")
else:
    print("No")