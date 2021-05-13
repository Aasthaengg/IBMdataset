import sys
input = sys.stdin.buffer.readline

N = int(input())
A = [[]] + [list(map(int, input().split()))[::-1] for _ in range(N)]

pair = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

stack = []
for i in range(1, N + 1):
  a = A[i].pop()
  pair[i][a] += 1
  if pair[i][a] == pair[a][i] == 1:
    stack.append(i)
    stack.append(a)

r = []
answer = 1
while stack:
  while stack:
    i = stack.pop()
    if A[i]:
      a = A[i].pop()
      pair[i][a] += 1
      if pair[i][a] == pair[a][i] == 1:
        r.append(i)
        r.append(a)
  stack = r
  if r:
    answer += 1
  r = []
  
flag = 1
for i in range(1, N + 1):
  if A[i]:
    flag = 0
    break
if flag:
  print(answer)
else:
  print(-1)