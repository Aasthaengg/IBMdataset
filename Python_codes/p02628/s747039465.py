N, K = map(int, input().split())
p = list(map(int, input().split()))
p = sorted(p, reverse=False)

sum = 0

for i in range(K):
    sum += int(p[i])
print(sum)