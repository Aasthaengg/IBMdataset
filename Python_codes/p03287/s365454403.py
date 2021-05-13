N,M = map(int,input().split())
A = list(map(int,input().split()))
sum_A = [0]*(N+1)
for i in range(N):
    sum_A[i+1] = sum_A[i] + A[i]

mod_M = {} # 累積和をMで割った余りがkey、そのような数の頻度がv
for sA in sum_A:
    r = sA%M
    if not r in mod_M:
        mod_M[r] = 1
    else:
        mod_M[r] += 1
ans = 0
for v in mod_M.values():
    ans += v*(v-1)//2
print(ans)