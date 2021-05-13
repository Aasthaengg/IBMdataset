while 1:
    a = int(input())
    if a == 0:
        break
    b = sum(a%10**(i+1)//10**i for i in range(1000) if a%10**i != a)
    print(b)
