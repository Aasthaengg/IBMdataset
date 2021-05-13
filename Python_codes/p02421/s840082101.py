count = int(input())
Taro_an = []
Hanako_an = []
Ts = 0
Hs = 0
for i in range(count) :
    animal = input().split(" ")
    Taro_an = animal[0]
    Hanako_an = animal[1]
    if Taro_an > Hanako_an :
        Ts += 3
    else :
        if Hanako_an > Taro_an :
            Hs += 3
        else :
            Ts += 1; Hs += 1
print(Ts,Hs)