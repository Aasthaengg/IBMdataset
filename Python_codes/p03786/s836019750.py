N = int(input())

A = list(map(int,input().split()))

A.sort()

memo = [0]*N

for i in range(N):
    memo[i] = memo[i-1]+A[i]

for i in range(N-1,0,-1):
    if A[i] <= 2 * memo[i-1]:
        ans = i-1
    else:
        break
print(N-ans)