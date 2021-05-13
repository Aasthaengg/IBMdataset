N=list(map(int,input().split()))
A=list(map(int,input().split()))
n=N[0]
k=N[1]
for i in range(n-k):
    if A[i]<A[k+i]:
        print("Yes")
    else:
        print("No")