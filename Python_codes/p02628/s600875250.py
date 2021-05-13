N,K = map(int,input().split())
p = list(map(int,input().split()))

p = sorted(p)

p = p[:K]

print(sum(p))