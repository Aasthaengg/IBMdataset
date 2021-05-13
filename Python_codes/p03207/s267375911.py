N = int(input())
p = [0]*N
for i in range(N):
  p[i] = int(input())
p.sort()
p[i] = p[i]//2
print(sum(p))