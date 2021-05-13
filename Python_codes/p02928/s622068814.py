N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for i in range(N):
    for j in range(i, N):
        if A[i] > A[j]:
            cnt += 1

cmb_cnt = 0
for a in A:
   cmb_cnt += len([x for x in A if x < a]) 

kC2 = (K*(K-1))//2
ans = (cnt*K)+(cmb_cnt*kC2)
print(ans%(10**9+7))
