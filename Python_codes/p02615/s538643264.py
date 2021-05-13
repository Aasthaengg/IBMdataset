N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
ans = 0
for i in range(N-1):
    ans += A[int((i+1)*0.5)]
    
print(ans)