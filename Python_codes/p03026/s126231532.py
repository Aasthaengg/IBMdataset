n = int(input())
nodes = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    nodes[a].append(b)
    nodes[b].append(a)
# print(nodes)

c = list(map(int, input().split()))
c.sort(reverse=True)
# print(c)

count = 0
answer = [0 for _ in range(n)]
for i in range(n):
  end = True
  for j in range(n):
    if len(nodes[j]) == 1:
      end = False
      nodes[nodes[j][0]].remove(j)
      nodes[j].pop()
      answer[j] = c.pop()
      count += answer[j]
  if end:
    break
print(sum(answer))

answer[answer.index(0)] = c.pop()
print(' '.join(map(str, answer)))
