#coding: UTF-8
import sys

H, W = map(int, input().split())
table = [[0]*(W+1) for i in range(H+1)]
# list = [[0 for i in range(W+1)] for j in range(H+1)]

for row in range(H):
    pre_table = list(map(int, input().split()))
    for col in range(W):
        table[row][col] = pre_table[col]

for row in range(H):
    for col in range(W):
        table[row][W] += table[row][col]

for col in range(W+1):
    for row in range(H):
        table[H][col] += table[row][col]

for row in range(H+1):
    print("%d"%(table[row][0]), end="")
    for col in range(1, W+1):
        print(" %d"%(table[row][col]), end = "")
    print()
