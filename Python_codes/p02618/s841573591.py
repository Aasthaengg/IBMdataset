import random
import numpy as np


D=int(input())
C=np.array(list(map(int,input().split())))
S=[]
for _ in range(D):
    S.append(list(map(int,input().split())))


T=[]
for i in range(D):
    print(np.argmax(S[i])+1)
