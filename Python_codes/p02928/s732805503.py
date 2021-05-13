N, K = map(int, input().split())
*A, = map(int, input().split())
MOD = 10**9+7

smaller = [0]*N
reverse = [0]*N
for i in range(N):
    for j in range(N):
        if j == i: continue
        if A[i] > A[j]:
            smaller[i] += 1
            if i < j:
                reverse[i] += 1

ans = (K*sum(reverse)%MOD + ((K*(K-1)//2)%MOD)*sum(smaller))%MOD
print(ans)