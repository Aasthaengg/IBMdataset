import math
X,Y,Z,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)
l=[]
#まずX+Yを求め、上から順にソート
#10^6相当の計算
for i in range(X):
    for j in range(Y):
        l.append(A[i] + B[j])
l.sort(reverse=True)
ans=[]
#(X+Y)+Zより、全体の上位を求めるが、Zが何であれ、X+Yの和が上からK番目以下のものは考慮しなくて良い
#(X+YにおいてK+i番目のもの(X+Y)_K+i+Zjが全体でK番以内に食い込めるということは、1~K番目のX+Yにて(X+Y)_1~K+Zj>(X+Y)_K+i+Zjが成立することと矛盾する)
#これで高々10^7相当までのソートでよくなる
for i in range(min(K,len(l))):
    for j in range(Z):
        ans.append(l[i]+C[j])
ans.sort(reverse=True)
for i in range(K):
    print(ans[i])