from collections import deque

N = int(input())
dif = []
for i in range(N):
    A,B = list(map(int,input().split()))
    dif.append((A+B,A,B))

dif.sort(key=lambda x: x[0])
Takahashi = 0
Aoki = 0
while dif:
    Takahashi += dif.pop()[1]
    if not dif:
        break
    Aoki += dif.pop()[2]

print(Takahashi-Aoki)