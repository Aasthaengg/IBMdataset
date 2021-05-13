A = int(input())
X = [input() for _ in range(A)]
B = int(input())
Y = [input() for _ in range(B)]
t = 0
for x in X:
  if X.count(x)-Y.count(x)>t:
    t = X.count(x)-Y.count(x)
  else:
    pass
print(t)