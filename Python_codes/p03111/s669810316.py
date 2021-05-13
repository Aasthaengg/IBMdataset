from itertools import combinations
n, a, b, c = map(int, input().split())
l = []
for i in range(n):
    l.append(int(input()))
ans = 10**6
f = lambda li, k: abs(sum(li)-k)+10*(len(li)-1)
for i in range(4**n):
    li = [[] for _ in range(4)]
    for j in range(n):
        li[(i//(4**j))%4].append(l[j])
    if len(li[0])*len(li[1])*len(li[2])==0:
        continue
    ans = min(ans, f(li[0], a)+f(li[1], b)+f(li[2], c))
print(ans)