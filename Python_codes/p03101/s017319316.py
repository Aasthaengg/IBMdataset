import sys
H,W = map(int,input().split())
h,w = map(int,input().split())
array = [[0]*W for I in range(H)]
# fill Horizone 1
for I in range(h):
    array[I] = [1]*W
# replace Horizone and Vertical
array = [list(x) for x in zip(*array)]
# fill Horizone 1
for I in range(w):
    array[I] = [1]*H
# replace Horizone and Vertical
array = [list(x) for x in zip(*array)]

count = 0
for I in range(H):
    count += array[I].count(0)
print(count)