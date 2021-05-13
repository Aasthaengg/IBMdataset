N=int(input())
num=[i for i in range(1,N+1)]
X=[]

for i in range(N):
    S,P=map(str,input().split())
    X.append([num[i],S,int(P)])

X = sorted(X,key=lambda d:d[2],reverse=True)
X = sorted(X,key=lambda d:d[1])

for i in X:
    print(i[0])