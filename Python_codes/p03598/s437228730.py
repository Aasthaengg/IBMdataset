# coding: utf-8
import math
#a, b, c = map(int,input().split())
N = int(input())
K = int(input())
#S = input()
ans = 0
#l = list(map(int,input().split()))
A = list(map(int,input().split()))

for i in range(N):
    ans += min(A[i], abs(K-A[i])) * 2

print(ans)