x,y = map(int,input().split())

#2^60 = 1,152,921,504,606,846,976 > 10^18ใงใใใ
for i in range(61):
    if y < x * 2**i:
        print(i)
        exit()

