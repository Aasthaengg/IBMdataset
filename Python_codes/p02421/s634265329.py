n = input()
a = [ raw_input().split() for _ in range(n)]
taro = 0
hanako = 0
for i in a:
    b = sorted(i)
    if i != b :
        taro += 3
    elif i[0] != i[1] :
        hanako += 3
    else :
        taro += 1
        hanako += 1
print taro,hanako