N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = 0

for x in range(N):
    C = A[0:x+1] + B[x:N]
    n = sum(C)
    ans = max(ans, n)

print(ans) 