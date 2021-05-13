N,A,B=map(int,input().split())
X=list(map(int,input().split()))
l=[]
for i in range(N-1):
    l.append(min((X[i+1]-X[i])*A,B))
print(sum(l))
