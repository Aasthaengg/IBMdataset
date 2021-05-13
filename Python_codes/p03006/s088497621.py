n = int(input())
x = [0]*n
y = [0]*n
for i in range(n): x[i],y[i] = map(int,input().split())

d = {(0,0):0}
for i in range(n-1):
    for j in range(i+1,n):
        dx = x[i]-x[j]
        dy = y[i]-y[j]
        d[(dx,dy)] = d.get((dx,dy),0) + 1
        d[(-dx,-dy)] = d.get((-dx,-dy),0) + 1
        
print(n-max(d.values()))