N = int(input())
A = list(map(int, input().split()))
i = 0
ans = 0
while i < N:
    j = i
    while j < N-1 and A[j]<=A[j+1]:
        j += 1
    k = i
    while k < N-1 and A[k]>=A[k+1]:
        k += 1
    ans += 1
    i = max(j, k) + 1
print(ans)
