x = int(input())
for i in range(1,10**8):
    if (i*(i+1)//2>=x):
        print(i)
        exit()