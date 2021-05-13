# -*- coding: utf-8 -*-
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N = int(readline())
data = []
X = []
for i in range(N):
    T, A = map(int, readline().split())
    data.append((T,A))

T_pre,A_pre = data[0] 
for i in range(1,N):
    T,A = data[i]
    n = max(-(-T_pre//T),-(-A_pre//A))
    T_pre = n*T
    A_pre = n*A
print(T_pre+A_pre)    