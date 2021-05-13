N, K, S = map(int, input().split())
ans = list()
for _ in range(K):
  ans.append(S)

for _ in range(N - K):
  ans.append(S + 1 if S != 10 ** 9 else S - 1)
  
print(' '.join(map(str, ans)))