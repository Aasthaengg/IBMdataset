N = int(input())
A = [-1]
ans = 0
for i in range(N):
    A.append(int(input()))
    if A[i+1] == 0:
        continue
    elif A[i+1] == A[i] + 1:
        ans += 1
    elif A[i+1] <= A[i]:
        ans += A[i+1]
    else:
        print(-1)
        exit()
print(ans)
