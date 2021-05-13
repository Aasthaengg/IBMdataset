n = int(input())
a = []
for i in range(n):
    a.append(list(map(str, input().split())))   
    
taro = []
hanako = []
for i in range(len(a)):
    if a[i][0] > a[i][1]:
        taro.append(3)
    elif a[i][0] == a[i][1]:
        taro.append(1)
        hanako.append(1)
    else:
        hanako.append(3)
print(sum(taro),sum(hanako))