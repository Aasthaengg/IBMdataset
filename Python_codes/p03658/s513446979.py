I = list(map(int, input().split()))
N, K = I[0], I[1]

ls = list(map(int, input().split()))
ls.sort(reverse=True)

MAX = 0
for i in range(K):
  MAX += ls[i]
  
print(MAX)