# coding: utf-8
import math
#N, M = map(int,input().split())
N = int(input())
#K = int(input())
#S = input()
ans = 0
flg = True
#l = list(map(int,input().split()))
#A = list(map(int,input().split()))
for i in range(N//4+1):
    amari = N - 4*i
    if amari%7 == 0:
        print("Yes")
        flg = False
        break
if flg:
    print("No")