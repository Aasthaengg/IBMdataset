# coding: utf-8
import math
N, K = map(int,input().split())
#N = int(input())
#K = int(input())
#S = input()
ans = 0
flg = True
#l = list(map(int,input().split()))
#A = list(map(int,input().split()))
if N%K == 0:
    print(0)
else:
    print(1)