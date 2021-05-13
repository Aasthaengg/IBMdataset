import sys

N, X = map(int, input().split())
L = input().split()
L = [int(i) for i in L]

d =0
count=1
for i in range(N):
    d = d+L[i]
    if d > X:
        print(count)
        sys.exit()
    count+=1
print(count)
