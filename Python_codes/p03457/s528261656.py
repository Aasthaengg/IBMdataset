n = int(input())
l = [list(map(int,input().split())) for i in range(n)]
t,x,y = [list(i) for i in zip(*l)]
p = 0
q = 0

for i in range(n):
    z = abs(p - (x[i] + y[i]))
    if ((t[i] - q) - z) % 2 == 0 and (t[i] - q) - z >= 0:
        p = x[i] + y[i]
        q = t[i]
    else:
        print('No')
        exit(0)

print('Yes')