c = [0]*4
for i in range(3):
        a,b = map(int,input().split())
        a,b = a-1,b-1
        c[a] += 1
        c[b] += 1
d = c.count(2)
print('YES') if d == 2 else print('NO')
