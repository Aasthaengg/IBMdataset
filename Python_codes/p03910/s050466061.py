n = int(input())
for i in range(1, n+1):
    if n <= (i+1)*i//2:
        x = (i+1)*i//2 - n
        for j in range(1, i+1):
            if j != x:
                print(j)
        exit()