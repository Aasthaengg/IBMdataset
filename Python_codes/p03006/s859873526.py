n = int(input())
x = [0]*n
y = [0]*n
for i in range(n): x[i],y[i] = map(int,input().split())

d = {(0,0):0}
for i in range(n):
    for j in range(n):
        if i == j: continue
        dx = x[i]-x[j]
        dy = y[i]-y[j]
        d[(dx,dy)] = d.get((dx,dy),0) + 1
        
print(n-max(d.values()))