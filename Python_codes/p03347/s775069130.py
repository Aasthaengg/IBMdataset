import sys

N = int(input())
A = [int(input()) for i in range(N)]

for i in range(N - 1):
    if A[i + 1] - A[i] > 1:
        print('-1')
        exit()

if A[0] != 0:
    print('-1')
    exit()

A.append(0)

count = 0
for i in range(N):
    if A[i+1] - A[i] <= 0:
        count += A[i]

print(count)
