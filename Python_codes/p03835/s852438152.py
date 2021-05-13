K,S = map(int,input().split())
x,y,z = 0,0,0
n = 0

for i in range(K+1):
    x = i
    for j in range(K+1):
        y = j
        z = S-(x+y)
        if 0 <= z <=K:
            n += 1

print(n)