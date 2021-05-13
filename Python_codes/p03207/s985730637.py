N = int(input())
p = []
for i in range(N):
  tmp = int(input())
  p.append(tmp)
p.sort(reverse=True)
p[0] /= 2
print(int(sum(p)))