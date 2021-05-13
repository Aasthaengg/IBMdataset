dataNum = 0
combNum = [0] * 100
while True:
    n,x=map(int, input().split())
    if n is x is 0:
        break
    else:
        for a in range(1,n-1):
            for b in range(a+1,n):
                for c in range(b+1,n+1):
                    calcResult = a + b + c
                    if calcResult == x:
                        combNum[dataNum] += 1
                    else:
                        pass
    dataNum += 1

for index in range(dataNum):
    print(combNum[index])
