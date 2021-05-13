n,m,X,Y=map(int,input().split())
x=[int(i) for i in input().split()]
y=[int(i) for i in input().split()]

for i in range(Y-X):
    z=X+1+i
    s="no_war"
    for j in range(n):
        if x[j]>=z:
            s="war"
            break
    for j in range(m):
        if y[j]<z:
            s="war"
            break
    if s=="no_war":
        print("No War")
        exit()
print("War")