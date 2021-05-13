N, K = map(int, input().split())
h = [int(x) for x in input().split()]

Cost = [0] * N
Cost[0] = 0

for i in range(1, N):
    tmp = [Cost[k] + abs(h[i] - h[k]) for k in range(max(0, i - K),i)]
    Cost[i] = min(tmp)

print(Cost[-1])