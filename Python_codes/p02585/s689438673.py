'''
4 4
4 1 2 3
-19 4 10 6

4 5
4 1 2 3
-19 4 10 6

4 8
4 1 2 3
-19 4 10 6
'''
n, k = map(int, input().split())
p = list(map(int, input().split()))
p = [i-1 for i in p]
c = list(map(int, input().split()))

minusOnly = True
for i in range(n):
    if c[i] > 0:
        minusOnly = False
        break

if minusOnly:
    print(max(c))
    exit()

ans = 0
used = [False]*n

for st in range(n):
    if not used[st]:
        gr = []
        now = st
        gr.append(st)
        used[st] = True
        while True:
            now = p[now]
            gr.append(now)
            used[now] = True
            if now == st:
                break
        gr.pop()

        cs = [c[i] for i in gr]
        s = sum(cs)
        point = 0
        r = k
        if r > 2*len(gr):
            if s > 0:
                point += s*(k//len(gr)-1)
                r -= len(gr)*(k//len(gr)-1)
            else:
                r = 2*len(gr)
        
        cs = cs + cs + cs
        plus = 0
        for i in range(len(gr)):
            nowSum = 0
            for g in range(r):
                nowSum += cs[i+g]
                plus = max(plus, nowSum)
        
        point += plus
        ans = max(ans, point)

print(ans)