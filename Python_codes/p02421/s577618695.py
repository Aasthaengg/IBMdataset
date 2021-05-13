n = int(input())
taro = 0
hanako = 0
for i in range(n):
    s = input().split(" ")
    if s[0] > s[1]:
        taro += 3
    elif s[0] < s[1]:
        hanako += 3
    else:
        taro += 1
        hanako += 1
print("{0} {1}".format(taro, hanako))