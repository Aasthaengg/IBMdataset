s = input()
t = input()

n = len(s)
m = len(t)

a = set(list(t))
b = set(list(s))

for x in a:
    if x not in b:
        print(-1)
        exit()

positions = [[0]*26 for i in range(n+1)]

for i in range(n):
    for j in range(26):
        if j == ord(s[-1-i])-97:
            positions[-2-i][j] = n-i
        else:
            positions[-2-i][j] = positions[-1-i][j]

roop = 0
p = 0
for i in range(m):
    a = ord(t[i])-97
    if positions[p][a]==0:
        roop += 1
        p = 0
    p = positions[p][a]

print(roop*n+p)