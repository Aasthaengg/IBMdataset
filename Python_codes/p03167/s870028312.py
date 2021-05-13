n,m=map(int,raw_input().split())
a=[list(raw_input().strip()) for _ in xrange(n)]
z=[[0]*(m+1) for _ in xrange(n+1)]
z[0][1]=1
for i in xrange(n):
    for j in xrange(m):
        if a[i][j]=='.':
            z[i+1][j+1]+=z[i+1][j]+z[i][j+1]
print z[-1][-1]%(pow(10,9)+7)