x = int(input())
flag = 0
for i in range((x//7)+1):
    if x < 0:
        break
    if x%4 == 0:
        flag = 1
    x = x - 7

if flag == 1:
    print("Yes")
else :
    print("No")