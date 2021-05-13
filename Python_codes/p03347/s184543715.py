

from functools import *
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def acinput():
    return list(map(int, input().split(" ")))


def II():
    return int(input())




N = int(input())
A = []
for i in range(N):
    A.append(II())


if A[0] >0:
    print(-1)
    sys.exit()

for i in range(1, N):
    if A[i]-A[i-1] > 1:
        print(-1)
        sys.exit()

count = 0
x = [0]*N

for i in range(0,N-1):
    if A[i]+1==A[i+1]:
        count+=1
    else:
        count+=A[i+1]

""" for i in reversed(range(N)):
    if A[i] != x[i]:
        for j in range(i-A[i], i):
            x[j+1] = x[j]+1
            count += 1

 """
print(count)
