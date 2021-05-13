n,k = map(int,input().split())
h = list(map(int,input().split()))

h.sort()
k = min(n,k)
for _ in range(k):
    h.pop()

print(sum(h))