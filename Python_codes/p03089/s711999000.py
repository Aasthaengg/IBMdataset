N = int(input())
A = list(map(int, input().split()))
for i in range(N):
    A[i] -= 1
ans = []
for _ in range(N):
    M = len(A)
    for i in range(M - 1, -1, -1):
        if A[i] > i:
            print(-1)
            exit()
        if A[i] == i:
            ans.append(A[i] + 1)
            A.pop(i)
            break
    if len(ans) == N:
        break
ans.reverse()
for a in ans:
    print(a)
