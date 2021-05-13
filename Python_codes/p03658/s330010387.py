N, K = map(int,input().split())

l = list(map(int,input().split()))
s = 0
for i in range(K):
    a = max(l)
    s += a
    l.remove(a)

print(s)
