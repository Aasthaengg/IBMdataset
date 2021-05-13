n, k = map(int, input().split())
p = list(map(int, input().split()))

p = list(map(lambda x: (1+x)/2, p))
s = [0]
num = 0
for i in range(n):
  num += p[i]
  s.append(num)
l = []
for i in range(n - k + 1):
  l.append(s[i+k]-s[i])

print(max(l))
