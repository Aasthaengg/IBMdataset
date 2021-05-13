N = int(input())
for i in range(1,N+1):
    if (i*(i+1))//2>=N:
        tmp = (i*(i+1))//2-N
        for j in range(1,i+1):
            if j != tmp:
                print(j)
        exit()