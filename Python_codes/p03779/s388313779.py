X = int(input())
for i in range(1000000):
    if X <= i*(i+1)//2:
        print(i)
        exit()