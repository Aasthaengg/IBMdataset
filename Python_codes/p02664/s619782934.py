def Int():
    return int(input())
def Ints():
    return map(int,input().split())
def IntList():
    return list(Ints())
def IntMat(N):
    return [IntList() for i in range(N)]

import sys
sys.setrecursionlimit(4100000)
rl = sys.stdin.readline

T = list(input())

for i in range(len(T)):
    if T[i] == '?':
        T[i] = 'D'
print(''.join(T))