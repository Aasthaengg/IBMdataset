N = int(input())
X = list(map(int,input().split()))
A = []

for p in range(1,101):
  A+=[sum((x-p)**2 for x in X)]

print(min(A))