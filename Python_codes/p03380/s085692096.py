N=int(input())
X=list(map(int,input().split()))
M=max(X)
X.remove(M)
m=min([abs(2*x-M) for x in X])
if (M+m)//2 in X:
    m=(M+m)//2
else:
    m=(M-m)//2
print(M,m)
