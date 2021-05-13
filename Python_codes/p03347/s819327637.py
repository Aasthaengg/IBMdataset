N = int(input())
A = [int(input()) for _ in range(N)]

ans = 0

if A[0] > 0:
    ans = -1
else:
    for i in range(N-1):
        if A[i] == A[i+1]-1:
            continue
        elif A[i] >= A[i+1]:
            ans += A[i]
        else:
            ans = -1
            break
    else:
        ans += A[N-1]

print(ans)