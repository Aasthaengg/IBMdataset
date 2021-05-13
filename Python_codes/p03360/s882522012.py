a, b, c = map(int, input().split())
K = int(input())
S = sum([a, b, c])
m = max([a, b, c])
S -= m
for i in range(K):
  m = m * 2
  #print(m)
print(S + m)
