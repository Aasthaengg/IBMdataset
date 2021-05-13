N=int(input())
A=list(map(int,input().split()))
AA=[]
for i in range(N):
    AA.append(1/A[i])
print(1/sum(AA))