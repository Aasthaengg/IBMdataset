n, m = map(int, input().split())
s = []
c = []
for i in range(n):
    s.append(list(map(int, input().split())))

for j in range(m):
    c.append(list(map(int, input().split())))
    
for k in range(n):
    cnt = []
    for l in range(m):
        kyori = abs(s[k][0]-c[l][0])+abs(s[k][1]-c[l][1])
        cnt.append(kyori)
    print(cnt.index(min(cnt))+1)