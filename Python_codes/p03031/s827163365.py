import itertools
n,m = map(int,input().split())
k = [list(map(int,input().split())) for _ in range(m)]
p = list(map(int,input().split()))
s = []
for i in range(n):
    s.append(i)
count = 0
for i in range(n+1):
    for item in itertools.combinations(s, i):
        li = [0] * m
        onoff = [0]*n
        for j in item:
            onoff[j] = 1
        for k_i in range(m):
            c = 0
            for k_j in range(k[k_i][0]):
                if onoff[k[k_i][k_j+1]-1] == 1:
                    c += 1
            if c % 2 == p[k_i]:
                li[k_i] = 1
        if all(li):
            count += 1
print(count)