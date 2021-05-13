taro, hanako = (0, 0)
for i in range(int(input())):
    t, h = input().strip().split()
    if t > h:
        taro += 3
    elif t < h:
        hanako += 3
    else:
        taro += 1
        hanako +=  1

print(taro, hanako)