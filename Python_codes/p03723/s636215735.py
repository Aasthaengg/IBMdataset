A = list(map(int, input().split()))
ans = 0
while A[0] % 2 == 0 and A[1] % 2 == 0 and A[2] % 2 == 0:
    if A[0] == A[1] and A[0] == A[2]:
        ans = -1
        break
    A[0], A[1], A[2] = ( A[1] + A[2] ) / 2, ( A[2] + A[0] ) / 2, ( A[0] + A[1] ) / 2
    ans += 1
print(ans)
