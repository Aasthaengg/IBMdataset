N = int(input())

L = []

for i in range(N):
    s,p = input().split()
    L.append([s, 100-int(p), i+1])
L.sort()
for j in L:
    print(j[2])