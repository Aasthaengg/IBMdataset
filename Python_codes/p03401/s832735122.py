n = int(input())
A = list(map(int,input().split()))

total = abs(A[0]) + abs(A[n-1])

for i in range(n-1):
    total += abs(A[1+i] - A[i])
    
for i in range(n):
    if i == 0:
        ans = total - abs(A[1]-A[0]) - abs(A[0]) + abs(A[1])
        
    elif i == n-1:
        ans = total - abs(A[i]-A[i-1]) - abs(A[i]) + abs(A[i-1])
        
    else:
        ans = total - abs(A[i]-A[i-1]) - abs(A[i+1]-A[i]) + abs(A[i+1]-A[i-1])
        
    print(ans)