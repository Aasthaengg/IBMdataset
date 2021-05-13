N=int(input())
A=list(map(int,input().split()))
B=[]
for i in range(N):
    B.append(A[i]-(i+1))

B.sort()
k=B[N//2]

C=map(lambda x:abs(x-k),B)
print(sum(C))
