N, K = map(int, input().split())
p = sorted(map(int, input().split()))
total = 0
for i in range(K) :
    total += p[i]
print(total)
