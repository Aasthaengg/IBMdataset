X,Y=map(int,input().split())
result = []
while Y >= X:
  result.append(X)
  X *= 2
print(len(result))