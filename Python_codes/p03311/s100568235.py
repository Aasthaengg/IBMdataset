N = int(input())
A = list(map(int,input().split(' ')))
num = 0
X = []
for i,j in enumerate(A):
  B = j-(i+1)
  X.append(B)
X.sort()
median = 0
if N % 2 == 0:
  median = (X[int(N/2)] + X[int(N/2-1)])/2
else:
  median = X[int((N-1)/2)] 

for x in X:
  num += abs(x-median)
print(int(num))    