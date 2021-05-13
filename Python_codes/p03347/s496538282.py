N = int(input())
A = [int(input()) for _ in range(N)]
if A[0] > 0:
    print(-1)
else:
    ans = 0
    for n in range(N-1, -1, -1):
        if A[n] - A[n-1] > 1 or A[n] > n:
            print(-1)
            break
        else:
            if A[n] - A[n-1] == 1:
                ans += 1
            else:
                ans += A[n]
    else:
        print(ans)
