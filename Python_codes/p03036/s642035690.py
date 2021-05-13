r,D,x = map(int,input().split())
X = [x]*11

for i in range(0,10):
  X[i+1] = r*X[i] - D
  
  
print(X[1])
print(X[2])
print(X[3])
print(X[4])
print(X[5])
print(X[6])
print(X[7])
print(X[8])
print(X[9])
print(X[10])