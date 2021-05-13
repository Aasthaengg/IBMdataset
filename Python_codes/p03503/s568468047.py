n = int(input())
f = []
for i in range(n):
    fi = list(map(int,input().split()))
    f.append(fi)
p = []
for i in range(n):
    t = list(map(int,input().split()))
    p.append(t)
ma = -1 * 10 ** 12
for bit in range(1024):
    count = 0
    countc = 0
    for i in range(n):
        countb = 0
        for j in range(10):
            if bit >> j & 1 and f[i][j] == 1:
                countb+=1
                countc+=1
        count+= p[i][countb]
    if countc == 0:
        continue
    ma = max(ma,count)
print(ma)