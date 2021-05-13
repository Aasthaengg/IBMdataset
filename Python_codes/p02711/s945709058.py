inter = list(input())
flag = 0
for i in range(0, len(inter)):
    if inter[i] == "7":
        flag = 1

if flag == 1:
    print("Yes")
else:
    print("No")