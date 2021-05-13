n, m, l = map(int,input().split())

x = []
y = []

for i in range(n):
    a = list(map(int,input().split()))
    x.append(a)
    
for i in range(m):
    b = list(map(int,input().split()))
    y.append(b)

#print(x)
a = 0
b = []
ans = []

for i in range(n):
    for j in range(l):
        for k in range(m):
            a += x[i][k]*y[k][j]
        #print(a)
        b.append(a)
        a = 0
    b = list(map(str, b))
    b = ' '.join(b)
    ans.append(b)
    b = []
        
[print(ans[i]) for i in range(len(ans))]
