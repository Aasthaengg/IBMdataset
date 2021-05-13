N, K = map(int, input().split())
l = [int(i) for i in input().split()]
a = 0
l.sort(reverse=True)
for i in range(K):
    a += l[i]
print(a)
