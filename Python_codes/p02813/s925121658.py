import math

NN = int(input())
AA = list(map(int,input().split()))
BB = list(map(int,input().split()))


AA_converted = 0
BB_converted = 0
LL = list(range(1,NN+1))
for ii in range(0,NN):
    AA_converted += math.factorial(NN-1-ii)*LL.index(AA[ii])
    LL.remove(AA[ii])
#    print(AA_converted)
#    print(LL)

LL = list(range(1,NN+1))
for ii in range(0,NN):
    BB_converted += math.factorial(NN-1-ii)*LL.index(BB[ii])
    LL.remove(BB[ii])
#    print(BB_converted)
#    print(LL)

print(abs(AA_converted-BB_converted))