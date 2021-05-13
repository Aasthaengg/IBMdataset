x = int(input())
for i in range(100000):
    if x<=i*(i+1)//2:
        print(i)
        exit(0)