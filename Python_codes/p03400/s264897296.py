import sys
N = int(input())
D,X = map(int,input().split())
array_A = []
for I in range(N):
    array_A.append(int(input()))

if not ( 1 <= N and D and X <= 100):
    sys.exit()
for J in range(len(array_A)):
    if not ( 1 <= array_A[J] <= 100):
        sys.exit()

count = 0
for K in range(len(array_A)):
    day = 1
    while day <= D:
        count += 1
        day += array_A[K]

print(count+X)