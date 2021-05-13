import sys
input = sys.stdin.readline

N=int(input())
a = []
for _ in range(N):
    a.append(int(input()))
found = [0]*N

steps = 0
i = 0
found[i] = 1
while True:
    j = a[i] - 1
    if found[j] == 1:
        print(-1)
        exit()
    steps += 1
    i = j
    found[i] = 1
    if i == 1:
        print(steps)
        exit()
