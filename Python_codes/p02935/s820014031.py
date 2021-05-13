input()
X = sorted(list(map(int, input().split())))
p = X[0]
for x in X[1:]:
  p = (p+x)/2
print(p)