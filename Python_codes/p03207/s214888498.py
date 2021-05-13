N = int(input())
p = []
for i in range(N):
    p.append(int(input()))

p[p.index(max(p))]=int(max(p)/2)
print(sum(p))
