n = int(input())
TARO = HANAKO = 0
for i in range(n):
    taro, hanako = input().split()
    if taro == hanako:
        TARO += 1
        HANAKO += 1
    elif taro > hanako:
        TARO += 3
    elif taro < hanako:
        HANAKO += 3
print(TARO, HANAKO)