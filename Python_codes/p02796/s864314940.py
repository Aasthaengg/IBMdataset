N=int(input())
A=[0]*N
for i in range(N):
    X,L=map(int,input().split())
    A[i]=(X-L,X+L)

A.sort(key=lambda x:x[-1])

K=0
x=-float("inf")

for a,b in A:
    if x<=a:
        K+=1
        x=b

print(K)