t = h = 0
for _ in range(int(input())):
    taro, hanako = input().split()
    if taro > hanako:
        t += 3
    elif hanako > taro:
        h += 3
    elif taro == hanako:
        t += 1
        h += 1
print(t, h)