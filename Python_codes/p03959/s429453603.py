N = int(input())
T = list(map(int,input().split()))
A = list(map(int,input().split()))
A.append(1)
count = 0
Tmax = 1
Amax = 1
T2 = [0] * N
A2 = [0] * N
ans = 1

for i in range(N):
    if T[i] > Tmax:
        Tmax = T[i]
        if A[i] > A[i+1]:
            Amax = A[i+1]
            if T[i] == A[i]:
                count = 1
            else:
                ans = 0
                break
        else:
            if T[i] > A[i]:
                ans = 0
                break
            else:
                count = 1
    else:
        if A[i] > A[i+1]:
            Amax = A[i+1]
            if A[i] > T[i]:
                ans = 0
                break
            else:
                count = 1
        else:
            count = min(A[i],T[i])
    ans *= count
    ans = ans % (10**9+7)
print(ans)