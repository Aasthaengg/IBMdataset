N, T = [int(i) for i in input().split()]
C = []

for i in range(N):
    C.append([int(i) for i in input().split()])

x = T
res = []

for c in C:
    cost = c[0]
    time = c[1]
    if time <= x:
        res.append(cost)
    

if len(res) == 0:
    print("TLE")
else:
    p = min(res)
    print(p)