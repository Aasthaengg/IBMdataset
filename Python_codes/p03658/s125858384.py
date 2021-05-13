N,K = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

sum = sum(l)
for i in range(N-K):
    sum-=l[i]
print(sum)