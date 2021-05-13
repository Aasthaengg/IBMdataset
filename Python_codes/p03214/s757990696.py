N = int(input())
A = list(map(int, input().split()))
mean = sum(A)/N

ans = 0
abs_value = abs(A[0] - mean)

for i in range(1, N):
    if abs(A[i] - mean) < abs_value:
        ans = i
        abs_value = abs(A[i] - mean)
    
print(ans)