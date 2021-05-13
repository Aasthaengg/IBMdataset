n,k = map(int, input().split())
al = list(map(int, input().split()))

als = sorted(al)
rl = als[n-k:]
print(sum(rl))