N = int(input())
A = [int(input()) for _ in range(N)]

count = 0
for i in range(N):
    if i == 0 and A[i] > 0:
        print(-1)
        exit()
    if A[i] == 0:
        continue
    else:
        if A[i] == (A[i-1] + 1):
            count += 1
        elif A[i] > A[i-1] + 1:
            print(-1)
            exit()
        else:
            count += A[i]

print(count)
