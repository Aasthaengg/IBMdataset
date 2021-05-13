N = int(input())
A = [int(input()) for _ in range(N)]
A.append(A[N-1])

ans = 0
for i in range(N-1, -1, -1):
    if A[i] > i or A[i+1]-A[i] >= 2:
        print(-1)
        exit()
    elif A[i+1]-A[i] == 1:
        continue
    else:
        ans += A[i]
print(ans)
