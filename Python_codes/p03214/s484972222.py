N = int(input())
A = [int(a) for a in input().split()]

mean = sum(A)/N
ans = 0

for i in range(N):
    if abs(mean-A[i]) < abs(mean-A[ans]):
        ans = i
        
print(ans)