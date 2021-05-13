N, K = map(int, input().split())
A = list(map(int, input().split()))
vis = [0]*N
p = 1
Town = []

while vis[p-1] == 0:
    Town.append(p)
    vis[p-1] = 1
    p = A[p-1]

l = Town.index(p)

if K < len(Town):
    print(Town[K])
else:
    print(Town[l + (K-l)%(len(Town[l:]))])