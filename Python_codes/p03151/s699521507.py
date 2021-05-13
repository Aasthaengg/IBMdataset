N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if sum(B) > sum(A):
    print(-1)

ab = [0]*N
for i in range(N):
    ab[i] = A[i]-B[i]

ab.sort()

ans = 0
minus_sum = 0
for i in range(N):
    if ab[i] >= 0:
        break
    minus_sum += ab[i]
    ans += 1

for i in reversed(range(N)):
    if minus_sum >= 0:
        print(ans)
        exit(0)

    minus_sum += ab[i]
    ans += 1

