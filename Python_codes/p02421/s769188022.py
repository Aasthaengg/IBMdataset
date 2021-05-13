n = int(input())
Taro_ten = 0
Hanako_ten = 0
for i in range(n) :
    a, b = list(input().split())
    Taro = list(a)
    Hanako = list(b)
    length = min(len(Taro), len(Hanako))
    for i in range(length) :
        if ord(Taro[i]) > ord(Hanako[i]) :
            Taro_ten += 3
            break
        elif ord(Taro[i]) < ord(Hanako[i]) :
            Hanako_ten += 3
            break
        if i == length -1 :
            if len(Taro) > length :
                Taro_ten += 3
            elif len(Hanako) > length :
                Hanako_ten += 3
            else :
                Taro_ten += 1
                Hanako_ten += 1
print(Taro_ten, Hanako_ten)
