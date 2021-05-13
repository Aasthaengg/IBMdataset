x, y = map(int, input().split())
flag = False
for i in range(0,x+1):
    j = x - i
    if i * 2 + j * 4 == y:
        flag = True
        break
if flag == True:
    print("Yes")
else:
    print("No")


