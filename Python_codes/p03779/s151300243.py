x = int(input())
for i in range(0,100000):
    ix = i*(i+1)/2
    if x <= ix :
        print(i)
        exit()
    else:
        pass