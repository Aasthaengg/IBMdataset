N, M, *_ = map(int, open(0).read().split())

A = []
K_i = 0
for i in range(N):
    K = _[K_i]
    A.append(_[K_i+1 :  K_i+1+K])
    K_i += K + 1
    
ans = 0

for m in range(1, M+1):
    for k, a_i in enumerate(A, start=1):
        if m not in a_i:
            break
        if k == len(A):
            ans += 1

print(ans)