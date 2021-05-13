n = int(input())


x = n / 2
result = 0

if n <= 10:
    result = n
elif (n <= 100 and not n % 10) or not x % 10:
    result = 0

    while(x > 0):
        result += int(x % 10)
        x = x // 10
    result = result* 2
else:
    if n % 10:
        x = n % 10
    elif n % 10: 
        x = n % 100
    elif n % 1000: 
        x = n % 1000
    elif n % 10000: 
        x = n % 10000
    n = n - x
    while(x > 0):
        result += x % 10
        x = x // 10

    while(n > 0):
        result += n % 10
        n = n // 10
print(result)


#
#else:
#    resulty, resultx = 0, 0
#
#    while(x > 0):
#        resultx += x % 10
#        x = x // 10
#
#    while(y > 0):
#        resulty += y % 10
#        y = y // 10
#
#    #print(resulty+resultx)
#    z = n//2
#
#    result = 0
#    while(z > 0):
#        result += z % 10
#        z = z // 10
#
#    if result*2 < resulty+resultx:
#        print(result*2)
#    else:
#        print(resulty+resultx)
#
