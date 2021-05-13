n, d =map(int,input().split())
for i in range(100):
    if (2 * d + 1)* i >= n:
        print(i)
        exit()
