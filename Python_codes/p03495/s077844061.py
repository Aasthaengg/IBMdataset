n, k = map(int, input().split())
a = list(map(int, input().split()))
p =  [0] * (n + 1)
for i in a:
  p[i] += 1
p.sort()
print(sum(p[:n-k+1]))