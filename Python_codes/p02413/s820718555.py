r,c=map(int,input().split())
a = [ [0]*(c+1) for i in range(0, r+1) ]
for i in range(0, r):
    a[i] = list(map(int, input().split()))
    a[i].append(sum(a[i]))
    for j in range(0, len(a[i])):
        a[r][j] += a[i][j]
    print(" ".join(map(str, a[i])))
print(" ".join(map(str, a[r])))