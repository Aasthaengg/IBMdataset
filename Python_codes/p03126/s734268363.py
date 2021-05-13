N,M=map(int,input().split())
l=list()
for i in range(N):
    A=list(map(int,input().split()))
    del A[0]
    l+=A
result=0
for i in range(M):
    if l.count(i+1)==N:
        result+=1
print(result)
