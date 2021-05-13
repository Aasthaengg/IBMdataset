n,k=map(int,input().split())
A=list(map(int,input().split()))

for i in range(n-k):
    nuke= A[i] 
    hairu= A[k+i] 
    print("YNeos"[nuke>=hairu::2])
