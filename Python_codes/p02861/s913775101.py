n = int(input())

X=[]
Y=[]
for i in range(n):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

D = []
for i in range(n):
    for j in range(i+1,n):
        D.append(((X[i]-X[j])**2+(Y[i]-Y[j])**2)**0.5)

# print(D)
ans = sum(D)*2/n
print(ans)