n=int(input())
a=[list(map(int,input().split())) for i in range(2)]
b=[[0 for i in range(n)] for j in range(2)]

for j in range(2):
    for i in range(n):
        if i==0:
            b[j][i]+=a[j][i]
        else:
            b[j][i]+=a[j][i]+b[j][i-1]

s=[0 for i in range(n)]
for i in range(n):
    if i==0:
        s[i]=b[0][i]+b[1][n-1]
    else:
        s[i]=b[0][i]+b[1][n-1]-b[1][i-1]

s.sort(reverse=True)
print(s[0])
