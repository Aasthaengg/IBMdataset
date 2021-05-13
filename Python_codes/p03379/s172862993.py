n=int(input())
x=list(map(int,input().split()))
X = sorted(x)
for i in range(n):
    if x[i] <= X[n//2-1]:
        print(X[n//2]) 
    elif x[i] >= X[n//2]:
        print(X[n//2-1])