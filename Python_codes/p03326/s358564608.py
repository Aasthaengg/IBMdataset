#100_D
n, m = map(int, input().split())
xyz = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(8):
    t = [-1, -1, -1]
    for j in range(3):
        if (i >> j) & 1:
            t[j] = 1
    
    l = [sum([xyz[i][k]*t[k] for k in range(3)]) for i in range(n)]
    l.sort(reverse= True)
    ans = max(ans, sum(l[:m]))
    
print(ans)