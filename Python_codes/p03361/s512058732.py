#coding: utf-8
#from collections import defaultdict, deque

H, W = (int(x) for x in input().split())

paint = []
for i in range(H):
    paint.append(list(input()))

def has_adjacent(i, j):
    for next_i, next_j in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
        if next_i < 0 or next_i >= H or next_j < 0 or next_j >= W:
            continue
        if paint[next_i][next_j] == '#':
            return True
    return False

for i in range(H):
    for j in range(W):
        if paint[i][j] == '#':
            if not has_adjacent(i, j):
                print("No")
                exit(0)

print("Yes")

