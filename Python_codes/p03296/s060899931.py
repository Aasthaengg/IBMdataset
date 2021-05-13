N = int(input())
A = [int(_) for _ in input().split()]

ans = 0
k = 1
for i in range(N-1):
    if A[i] == A[i+1]:
        k += 1
    else:
        ans += k // 2
        k = 1
ans += k // 2
print(ans)
