import copy
n , m , q = map(int,input().split())

a = [0]*q
b = [0]*q
c = [0]*q
d = [0]*q
for i in range(q):
    a[i],b[i],c[i],d[i] = map(int, input().split())

AA = [[1]*n]

while True:
    for i in reversed(range(n)):
        if AA[-1][i] != m:
            break
    else:
        break
    tmp = copy.deepcopy(AA[-1])
    tmp[i:] = [tmp[i]+1]*(n-i)
    AA.append(tmp)

ans = 0
for i in range(len(AA)):
    pt = 0
    for j in range(q):
        if AA[i][b[j]-1] - AA[i][a[j]-1] == c[j]:
            pt = pt + d[j]
    ans = max(ans,pt)
    
print(ans)