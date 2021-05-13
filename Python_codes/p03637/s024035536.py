n = int(input())
lis = list(map(int, input().split()))

b = [0]*3

for i in lis:
    if i % 4 == 0:
        b[2] += 1
    elif i % 2 == 0:
        b[1] += 1
    else:
        b[0] += 1

if b[1] == 0:
    if b[2] + 1 >= b[0]:
        print("Yes")
        exit()
    else:
        print("No")
        exit()



if b[2]  >= b[0]:
    print("Yes")
else:
    print("No")
