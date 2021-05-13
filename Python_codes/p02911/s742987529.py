N,K,Q = map(int, input().split())
A = []
for _ in range(Q):
    A.append(int(input()))

p = [0] * N
for a in A:
    p[a-1] += 1

for i in range(N):
    p[i] = K-(Q-p[i])
    if p[i] <= 0:
        print('No')
    else:
        print('Yes')
