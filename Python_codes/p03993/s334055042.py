N=int(input())
A=list(map(int, input().split()))
count=0
for i in range(N):
    a=A[i]-1
    if a>i and A[a]==i+1:
        count+=1
print(count)