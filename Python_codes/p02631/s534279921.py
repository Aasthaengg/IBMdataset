N = int(input())

A = list(map(int,input().split()))

ans = A[0]

for i in range(1,N):
    ans = ans ^ A[i]

memo = []

for i in range(N):
    memo.append(ans ^ A[i])

print(*memo)