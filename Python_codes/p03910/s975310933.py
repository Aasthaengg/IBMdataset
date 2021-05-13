n = int(input())
for i in range(1,n+1):
    if i*(i+1)//2>=n:
        for j in range(1,i+1):
            if j!=i*(i+1)//2-n:
                print(j)
        break