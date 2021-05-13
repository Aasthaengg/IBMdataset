n = int(input())
flag = False
for t in range(0,25):
    for i in range(0,15):
        if t !=0 or i != 0:
            if t*4 + i*7==n:
                flag = True
if flag :
    print("Yes")
else :
    print("No")