N, K = map(int, input().split())
l = list(map(int, input().split()))

l = sorted(l, reverse=True)
cn = 0
for i in range(K):
    cn = cn + l[i]
    
print(cn)
