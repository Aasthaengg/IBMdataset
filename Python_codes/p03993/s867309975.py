N=int(input())
A=["*"]+list(map(int,input().split()))

T=0
for i in range(1,N+1):
    T+=(A[A[i]]==i)
print(T//2)
