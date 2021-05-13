N=int(input())
X=list(map(int,input().split()))
Y=sorted(X)
l,r=Y[N//2-1],Y[N//2]
for i in X:
    if l < i:
        print(l)
    else:
        print(r)