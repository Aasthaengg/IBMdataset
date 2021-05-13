def cin():  return list(map(int,input().split()))

N, K = cin()
A = cin()
INF = 10 ** 9 + 7

cnt1 = 0
l = len(A)
for i in range(l):
    for j in range(i + 1, l):
        cnt1 += (A[i] > A[j])
        
AA = A + A
l = len(AA)
cnt2 = 0
for i in range(l):
    for j in range(i + 1, l):
        cnt2 += (AA[i] > AA[j])

ans = K * cnt1 + (cnt2 - 2 * cnt1) * K * (K - 1) // 2
print(ans % INF)