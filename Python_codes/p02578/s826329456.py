N=int(input())
A=list(map(int,input().split()))
count=0
for num in range(N-1):
    if A[num]>A[num+1]:
        count=count+A[num]-A[num+1]
        A[num+1]=A[num]
    else:
        continue        
print(count)  