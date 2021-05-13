#import math
#import numpy as np
#import torch
#import torch.nn as nn
#import matplotlib.pyplot as plt
#from decimal import Decimal

#N=int(input())
A,V = map(int,input().split())
B,W = map(int,input().split())
T=int(input())
#A = list(map(int,input().split()))
#S=str(input())

if V<=W:
    print('NO')
else:
    L=abs(A-B)
    if L/(V-W)<=T:
        print('YES')
    else:
        print('NO')
