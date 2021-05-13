N, K = map(int, input().split())

n = []
for i in range(N):
    n.append(i)

num = 0
ind = 0
while (len(n) - K) >= 0:
    n.pop(0)
    num += 1

print(num)
