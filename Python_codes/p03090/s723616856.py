n = int(input())
es = []
if n%2==0:
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if j!=n+1-i:
                es.append((i, j))
else:
    for i in range(1, n):
        for j in range(i+1, n):
            if j!=n-i:
                es.append((i, j))
    for i in range(1, n):
        es.append((i, n))
print(len(es))
for i,j in es:
    print(i,j)