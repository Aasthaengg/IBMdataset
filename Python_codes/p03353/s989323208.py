S = input()
K = int(input())
N = len(S)

x = set(list(S))

for i in range(K):
  for j in range(N-i):
    x.add(S[j:j+i+1])

x = list(x)
x.sort()
print(x[K-1])