a, b = map(int, input().split())
for i in range(50):
    if  a * i  - (i-1) >= b:
        print(i)
        exit()