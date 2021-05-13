n, m, p = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(m)]
 
for i in range(m):
    lst[i][2] = - (lst[i][2] - p)

d = [10**100] * (n+1)
d[1] = 0
rep = 0
 
while True:
    update = False
    for edge in lst:
        a,b,c = edge
        if d[a] != 10**100 and d[b] > d[a]+ c:
            if rep >= n:
                d[b] = -10**100
            else:
                d[b] = d[a] + c
            update = True
    if not update:
        break
    rep += 1
    if rep > 2*n:
        break

if d[n] <= - 10**100:
    print(-1)
elif -d[n] < 0:
    print(0)
else:
    print(-d[n])