N = int(input())
A = [0] * N
for i in range(N):
    A[i] = int(input())

if A[0] != 0:
    print(-1)
    exit()

ans = 0
for i in range(1,N):
    if A[i] == A[i-1] + 1:
        ans += 1
    elif A[i] < A[i-1] + 1:
        ans += A[i]
    else:
        print(-1)
        exit()
    
print(ans)