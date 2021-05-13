n=int(input())
A=list(map(int,input().split()))
count=0
i=0
while i < n:
    j=i
    while j < n-1 and A[j]<=A[j+1]:
        j += 1
    k=i
    while k < n-1 and A[k]>=A[k+1]:
        k += 1
    count += 1
    i = max(j,k)+1
print(count)