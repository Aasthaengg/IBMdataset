while True:
    Num,Total = map(int,input().split())
    if Num == 0 and Total == 0:
        break
    Count = 0
    for i in range(1,Num+1):
        for j in range(i+1,Num+1):
            for k in range(j+1,Num+1):
                if i + j + k == Total:
                    Count += 1
    print(Count)