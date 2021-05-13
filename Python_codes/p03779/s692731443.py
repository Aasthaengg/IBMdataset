x = int(input())
for i in range(10**6):
    if i*(i+1)//2 >= x:
        print(i)
        exit()
