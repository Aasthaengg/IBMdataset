r,c=map(int,input().split())
a,b=[],[0]*c
for i in range(r):
    x=list(map(int,input().split()))
    print(*x, end=' ')
    print(sum(x))
    for j in range(c):
        b[j]+=x[j]
print(*b, end=' ')
print(sum(b))