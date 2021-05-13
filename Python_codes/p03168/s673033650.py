n=int(input())
h=list(map(float,input().split()))
t=[]
for i in range(n+1):
    temp=[1]*(n+1)
    t.append(temp)
for i in range(1,n+1):
    for j in range(i+1):
        if j==0:
            t[i][j]=t[i-1][0]*(1-h[i-1])
        elif i==j:
            t[i][j]=t[i-1][j-1]*(h[i-1])
        else:
            t[i][j]=(t[i-1][j-1]*(h[i-1]))+(t[i-1][j]*(1-h[i-1]))
a=0
for i in range(n//2+1,n+1):
    a+=t[n][i]
print(a)