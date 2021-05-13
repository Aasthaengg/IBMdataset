N,K = map(int,input().split())
p = 0
for i in range(1,N+1):
    j = i
    total = 0
    while (j < K):
        total += 1
        j *= 2
    p += (0.5**total) / N
print(p)