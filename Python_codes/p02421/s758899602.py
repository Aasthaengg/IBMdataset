taro = hanako = 0
for i in range(int(input())):
    tcard, hcard = input().split()
    if tcard == hcard:
        taro += 1
        hanako += 1
    elif tcard > hcard:
        taro += 3
    else:
        hanako += 3

print('%d %d' %(taro, hanako))