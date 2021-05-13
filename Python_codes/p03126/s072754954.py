N,M=map(int,input().split())
foods=[N]*M
for i in range(N):
    A=list(map(int,input().split()))
    K=A.pop(0)
    for j in A: foods[j-1]-=1
print(foods.count(0))