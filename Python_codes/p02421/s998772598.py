taro_point=0
hanako_point=0
n=int(input())
for i in range(n):
    taro_card,hanako_card=input().split()
    if taro_card>hanako_card:
        taro_point+=3
    elif taro_card<hanako_card:
        hanako_point+=3
    else:
        taro_point+=1
        hanako_point+=1
print(taro_point,hanako_point)
