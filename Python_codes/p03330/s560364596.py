from collections import defaultdict
n,c = map(int,input().split())
d = [0]
for i in range(c):
    d.append([0] + list(map(int,input().split())))
li0 = []
li1 = []
li2 = []
for i in range(n):
    g = list(map(int,input().split()))
    for j in range(n):
        if (i + j) % 3 == 0:
            li0.append(g[j])
        if (i + j) % 3 == 1:
            li1.append(g[j])
        if (i + j) % 3 == 2:
            li2.append(g[j])
dic0 = defaultdict(int)
dic1 = defaultdict(int)
dic2 = defaultdict(int)
for i in li0:
    dic0[i] += 1
for i in li1:
    dic1[i] += 1
for i in li2:
    dic2[i] += 1 
ans = 1000000000
for i in range(1,c+1):
    for j in range(1,c+1):
        for k in range(1,c+1):
            if i == j or j == k or i == k:
                continue
            x = 0
            for color in range(1,c+1):
                x += dic0[color] * d[color][i]
                x += dic1[color] * d[color][j]
                x += dic2[color] * d[color][k]
            ans = min(x,ans) 
print(ans) 
