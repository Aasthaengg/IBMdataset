n = int(input())
p = [0] * n
for i in range(n):
  p[i]= int(input())
p.sort()
print(p[-1]//2 + sum(p[:-1]))