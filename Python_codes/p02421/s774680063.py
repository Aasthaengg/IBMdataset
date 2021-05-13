num = int(input())
taro, hanako = 0 ,0
for i in range(num):
    lst = list(map(str, input().split()))
    while 1:
        if lst[0] == lst[1]:
            taro = taro + 1
            hanako = hanako + 1
            break
        else:
            length = min(len(lst[0]),len(lst[1]))
            for j in range(length):
                first = ord(lst[0][j:j+1])
                second = ord(lst[1][j:j+1])
                if first > second:
                    taro = taro + 3
                    break
                elif first < second:
                    hanako = hanako + 3
                    break
                elif j == length - 1:
                    if len(lst[0]) > len(lst[1]):
                        taro = taro + 3
                    elif len(lst[0]) < len(lst[1]):
                        hanako = hanako + 3
                    break
            break
print(str(taro) + " " + str(hanako))
