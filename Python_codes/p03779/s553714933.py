x = abs(int(input()))

for i in range(1, x+1):
    total = 1/2 * i * (i+1)
    if total >= x:
        print(i)
        exit()