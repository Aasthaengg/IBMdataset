N,K = map(int,input().split())
h = sorted([int(input()) for _ in range(N)])

l = []
for i in range(N-K+1):
    l.append(h[i+K-1]-h[i])

print(min(l))