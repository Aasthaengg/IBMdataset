N = int(input().rstrip())
A = list(map(int,input().rstrip().split()))
ans = 0
for i in range(N):
    ans += 1/A[i]
print(1/ans)