n = int(input())

sp = []

for i in range(n):
    si, pi = list(input().split())
    sp.append([si, -int(pi), i+1])

sp.sort()

for i in range(n):
    print(sp[i][2])