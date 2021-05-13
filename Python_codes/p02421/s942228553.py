n = input()
taro = 0
hanako = 0
for i in range(n):
    x = map(str, raw_input().split())
    #print x[0]
    #print x[1]
    if(x[0] > x[1]):
        taro += 3
    elif(x[0] == x[1]):
        taro += 1
        hanako += 1
    else:
        hanako += 3
print '%d %d' %(taro, hanako)

exit(0)