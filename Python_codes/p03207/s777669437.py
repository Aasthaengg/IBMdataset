N = int(input())
p = []
for i in range(N):
  p.append(int(input()))

p.sort()
print(sum(p[:-1]) + int(p[-1]/2))