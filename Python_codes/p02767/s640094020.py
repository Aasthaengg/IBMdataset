N=int(input())
X=list(map(int,input().split()))
a=round(sum(X)/N)
Y=[]
for i in X:
    Y.append((i-a)**2)
print(sum(Y))