N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

ans = 0
for i in range(N):
    ans = max(ans,sum(A[:i])+sum(B[i:])+A[i])

print(ans)
