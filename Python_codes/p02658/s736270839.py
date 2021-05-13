n = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

ans = 1

for a in A:
    if A[n-1] == 0:
        ans = 0
        break
    ans *= a
    if ans > 10**18:
        ans = -1
        break

print(ans)