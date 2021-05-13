a,b = input().split()
x = int(a+b)
flag = 0
for i in range(400):
    if i**2==x:
        flag = 1
        break
if flag==1:
    print("Yes")
else:
    print("No")