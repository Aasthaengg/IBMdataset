N = int(input())
SPI = [input().split()+[i] for i in range(N)]
SPI.sort(key=lambda x:(x[0], -int(x[1])))
for _,_,i in SPI:
    print(i+1)