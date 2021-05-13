a = ord('a')

s = [ord(x)-a for x in list(input())]
t = [ord(x)-a for x in list(input())]

n = len(s)
m = len(t)

positions = [[0]*26 for i in range(n+1)]

for i in range(n):
    for j in range(26):
        if j == s[-1-i]:
            positions[-2-i][j] = n-i
        else:
            positions[-2-i][j] = positions[-1-i][j]

roop = 0
p = 0
flag = 1
for i in range(m):
    a = t[i]
    if positions[p][a]==0:
        roop += 1
        p = 0
    p = positions[p][a]
    if p == 0:
        flag = 0
        break

print(roop*n+p if flag else -1)