A,B,C,D = [int(input()) for i in range(4)]
#電車安い方
train = min(A,B)          
#バス安い方
bus = min(C,D)
sum = train + bus
print(sum)