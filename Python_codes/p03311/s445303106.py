N = int(input())
A = list(map(int,input().split()))
for i in range(N):
    A[i] -= i + 1
A.sort()
dis = A[-(-N // 2) - 1]
ans = 0
for i in range(N):
    ans += abs(A[i] - dis)
print(ans)