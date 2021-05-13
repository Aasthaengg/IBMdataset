N = int(input())
X = list(map(int, input().split()))
X = sorted(X)
avg = sum(X)//N
aa = []
for i in range(2):
  avg = avg + i
  a = 0
  for j in range(N):
    a += (X[j] - avg)**2
  aa.append(a)
print(min(aa))