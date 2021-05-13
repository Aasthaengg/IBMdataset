a, b = (int(i) for i in input().split())  

if a == b: 
    print(-1)
elif a < 0 or b < 0: 
    print (-1)
else:
    for i in range(1, int(10 ** 10 / a)):
        if a * i % b != 0:
            print(a * i)
            exit()
        else:
            continue
    print(-1)
