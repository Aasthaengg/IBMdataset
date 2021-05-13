import sys

input_line = [int(x) for x in input().split()]
N = input_line[0]
H = input_line[1]
W = input_line[2]

A = [[int(x) for x in input().split()] for x in range(N)]

cnt = 0
#A[[10,3],[5,2],[2,5]]
for _ in range(N):
    if A[_][0] // H > 0 and A[_][1] // W > 0:
        cnt += 1

print(cnt)