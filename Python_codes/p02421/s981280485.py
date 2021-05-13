taro_score = 0
hanako_score = 0

for i in range(int(input())):
    taro,hanako = input().split()
    if taro < hanako:
        hanako_score += 3
    elif taro > hanako:
        taro_score += 3
    else:
        taro_score += 1
        hanako_score += 1
        
print(str(taro_score),str(hanako_score))