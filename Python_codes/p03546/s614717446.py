from itertools import permutations
h, w = map(int, input().split())
c = []
for _ in range(10):
    c.append(list(map(int, input().split())))
a = [0]*10
for _ in range(h):
    for i in map(int, input().split()):
        if i<0:
            continue
        a[i] += 1
ans = 0    
for i in range(10):
    if i==1 or a[i]==0:
        continue
    mi = c[i][1]
    li = [k for k in range(10) if k!=1 and k!=i]
    for j in range(1, 9):
        for p in permutations(li, j):
            pre = i
            tmp = 0
            for now in p:
                tmp += c[pre][now]
                pre = now
            tmp += c[pre][1]
            if tmp < mi:
                mi = tmp
    ans += mi*a[i]
print(ans)