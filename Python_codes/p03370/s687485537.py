import sys
N,X = map(int,input().split())
array_m = []
for I in range(N):
    array_m.append(int(input()))

if not (2 <= N <= 100):
    sys.exit()


base = 0
for J in range(N):
    if not ( 1<= array_m[J] <= 1000):
        sys.exit()
    base += array_m[J]

if not(1 <= base <= 10 ** 5):
    sys.exit()

print(int(N + (X - base) / min(array_m)))