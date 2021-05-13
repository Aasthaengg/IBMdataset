a_red,b_green,c_blue = list(map(int,input().split()))
kai = int(input())

for i in range(kai+1):
    if a_red >= b_green:
        b_green = b_green *2
    elif b_green >= c_blue:
        c_blue = c_blue *2
    else:
        print("Yes")
        exit()
print("No")