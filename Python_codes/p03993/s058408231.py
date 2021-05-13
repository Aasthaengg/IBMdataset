N=int(input())
A=list(map(int,input().split()))
count=0
for i in range (N):
    if A[i]<i+1:
        continue
    K=A[i]
    if A[K-1]==i+1:
        count+=1

print(count)