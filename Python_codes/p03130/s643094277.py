x = list(map(int,(input().split())))
y = list(map(int,(input().split())))
z = list(map(int,(input().split())))
count1 =  0
count2 =  0
count3 =  0
count4 =  0

num = x + y + z

for i in range(len(num)):
    
    if num[i] == 1:
        count1 += 1
        if count1 >=3:
            print("NO")
            exit()
    if num[i] == 2:
        count2 += 1
        if count2 >=3:
            print("NO")
            exit()
    if num[i] == 3:
        count3 += 1
        if count3 >=3:
            print("NO")
            exit()
    if num[i] == 4:
        count4 += 1
        if count4 >=3:
            print("NO")
            exit()

print("YES")

