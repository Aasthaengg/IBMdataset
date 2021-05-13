N, K = list(map(lambda n: int(n), input().split(" ")))
A = []
for i in range(K):
  d = int(input())
  for x in list(map(lambda m: int(m), input().split(" "))):
  	A.append(x)
print(N - len(set(A)))