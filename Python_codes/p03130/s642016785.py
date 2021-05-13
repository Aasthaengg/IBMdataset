c = [0]*4
for i in range(3):
    a,b = map(int,input().split())
    c[a-1] += 1
    c[b-1] += 1
c.sort()
print('YES' if c==[1,1,2,2] else 'NO')