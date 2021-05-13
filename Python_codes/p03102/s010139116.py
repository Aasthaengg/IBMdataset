import math
a,b,c= map(int,input().split())
d = list(map(int,input().split()))
answer = 0
e = [list(map(int,input().split()))for i in range(a)]
for i in range(a):
    g = 0
    for j in range(b):
        g += e[i][j]*d[j]
    g += c
    if g>0:
        answer += 1
print(answer)