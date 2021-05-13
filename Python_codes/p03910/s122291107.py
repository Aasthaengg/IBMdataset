n = int(input())

for i in range(1,n+1):
    if i*(i+1)//2 >=n:
        k = i*(i+1)//2 - n
        for j in range(1,i+1):
            if j == k:
                continue
            else:
                print(j)
        exit()


