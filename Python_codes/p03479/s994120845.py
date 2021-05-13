X,Y = map(int,input().split())
div = Y//X
bitnum = bin(div)
print(len(bitnum)-2)