n = int(input())
A = list(map(int,input().split()))

ans = float('inf')
arai = sum(A)
sunuke = 0
for i in range(n-1):
    sunuke += A[i]
    arai -= A[i]
    ans = min(ans, abs(sunuke-arai))

print(ans)