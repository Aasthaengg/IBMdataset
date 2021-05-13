N, K = list(map(int, input().split()))
h = list()
for i in range(N):
    h.append(int(input()))

h.sort()

ans_l = list()
for i in range(N-K+1):
    ans_l.append(h[i+K-1]- h[i])

print(min(ans_l))