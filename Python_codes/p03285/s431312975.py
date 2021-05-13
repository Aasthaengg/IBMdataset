N =int(input())
flag = False
for i in range(N):
    for j in range(N):
        if(4*i+7*j==N):
            flag=True
            break
    if(flag):
        break
if(flag):
    print("Yes")
else:
    print("No")