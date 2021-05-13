import sys

n,k = map(int,input().split())
x = k+(n%k)
min = sys.maxsize

while True:
    if x%k == 0:
        min = 0
        break

    x = abs(x-k)
    if x == min :break
    elif x < min : min = x

print(min)
