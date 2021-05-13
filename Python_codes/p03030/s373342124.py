import numpy as np
N = int(input())
List = [[]]*N
for T in range(0,N):
    Str,Num = input().split()
    List[T] = [Str,int(Num),T+1]
SorL = sorted(List, key=lambda x:(x[0],-x[1]))
SorI = list(str(x[2]) for x in SorL)
print('\n'.join(SorI))