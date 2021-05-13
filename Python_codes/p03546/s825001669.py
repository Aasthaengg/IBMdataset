from collections import Counter

H, W = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
a = []
for i in range(H):
    a += list(map(int, input().split()))

cost = [10**5]*10
cost[1] = 0
temp = [['1', 0]]

while temp:
    p = temp.pop()
    if len(p[0]) < 10:
        for s in '0123456789':
            if s in p[0]:continue
            else:
                nxt = p[1] + c[int(s)][int(p[0][-1])]
                if cost[int(s)] > nxt:
                    temp.append([p[0] + s, nxt])
                    cost[int(s)] = nxt
        
d = Counter(a)
ans = 0
for i in range(10):
    ans += d[i]*cost[i]
print(ans)