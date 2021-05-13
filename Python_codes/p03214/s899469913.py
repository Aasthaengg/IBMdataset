N = int(input())
a = list(map(int, input().split()))

avg = sum(a)/len(a)
dist = []
for i in range(N):
    dist.append(abs(a[i]-avg))

print(dist.index(min(dist)))