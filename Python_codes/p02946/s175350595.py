K, X = map(int, input().split())
l = []
for i in range(2*K-1):
  l.append(X-(K-1)+i)
for i in range(len(l)):
  l[i] = str(l[i])
result = ' '.join(l)
print(result)