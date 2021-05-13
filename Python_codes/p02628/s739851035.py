N, K = map(int, input().split())
p = input("").split()
p = [int(i) for i in p]
p = sorted(p)

M = sum(p[0:K])
print(M)
