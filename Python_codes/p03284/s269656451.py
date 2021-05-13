n,k = map(int,input().split())
p = [0 for _ in range(k)]
for i in range(n):
    index = i%k
    p[index] += 1
print(max(p)-min(p))