N,K = [int(x) for x in input().split()]
h = [0 for x in range(N)]
for i in range(N):
    h[i] = int(input())
h = sorted(h)
dis = []
for i in range(N-K+1):
    dis.append(h[i+K-1]-h[i])
print(min(dis))
