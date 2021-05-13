n = int(input())
for i in range(1, n+1):
    if i % 3 == 0:
        print(' '+str(i), end = '')
    elif i % 10 ==3:
        print(' '+str(i), end = '')
    else:
        x = i
        while x != 0:
            x = x // 10
            if x % 10 == 3:
                print(' '+str(i), end = '')
                break
print('')