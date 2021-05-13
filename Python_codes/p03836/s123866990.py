SX,SY,TX,TY = (int(T) for T in input().split())
print('R'*(TX-SX)+'U'*(TY-SY)+'L'*(TX-SX)+'D'*(TY-SY)+'D'+'R'*(TX-SX+1)+'U'*(TY-SY+1)+'L'+'U'+'L'*(TX-SX+1)+'D'*(TY-SY+1)+'R')