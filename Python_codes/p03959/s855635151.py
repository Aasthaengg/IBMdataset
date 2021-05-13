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
    if T[i] > Tmax and A[i] > A[i+1] and T[i] != A[i]:
        ans = 0
        break
    elif T[i] > Tmax and A[i] > A[i+1] and T[i] == A[i]:
        count = 1
        Tmax = T[i]
        Amax = A[i+1]
    elif T[i] > Tmax and A[i] == A[i+1] and T[i] > A[i]:
        ans = 0
        break
    elif T[i] > Tmax and A[i] == A[i+1] and T[i] <= A[i]:
        count = 1
        Tmax = T[i]
    elif T[i] == Tmax and A[i] > A[i+1] and A[i] > T[i]:
        ans = 0
        break
    elif T[i] == Tmax and A[i] > A[i+1] and A[i] <= T[i]:
        count = 1
        Amax = A[i+1]
    else:
        count = min(A[i],T[i])
    ans *= count
    ans = ans % (10**9+7)
print(ans)