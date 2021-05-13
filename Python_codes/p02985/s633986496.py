N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N - 1)]

MOD = 10 ** 9 + 7

graph = [[] for _ in range(N + 1)]
for A, B in AB:
  graph[A].append(B)
  graph[B].append(A)
#print("graph:", graph)

parent = [-1] * (N + 1)

stack = [1]
parent[1] = 0
while stack:
  s = stack.pop()
  for g in graph[s]:
    if parent[s] != g:
      parent[g] = s
      stack.append(g)
#print("parent:", parent)

cnt = [0] * (N + 1)
for i in range(2, len(parent)):
  cnt[parent[i]] += 1
#print("cnt:", cnt)

P = [1]
for i in range(N + 2):
  P.append((P[-1] * (K - 2 - i)) % MOD)
#print("P:", P)

answer = K
for i in range(1, len(cnt)):

  M = cnt[i]
  if M == 0:
    continue  
  #print("M, answer :", M, answer)

  if i == 1:
    if K - 1 >= M:
      for j in range(cnt[1]):
        answer *= (K - 1 - j)
        answer %= MOD
    else:
      answer = 0
  else:
    if K - 2 >= M:
      answer *= P[M]
      answer %= MOD
    else:
      answer = 0
print(answer)      