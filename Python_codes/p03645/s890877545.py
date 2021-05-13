N, M = map(int, input().split())
a = [0] * M
b = [0] * M
list = []
for i in range(M):
  a[i], b[i] = map(int, input().split())
for i in range(M):
  if a[i] == 1:
    list.append(b[i])
  elif b[i] == N:
    list.append(a[i])
list = sorted(list)
ans = 'IMPOSSIBLE'
for i in range(len(list)-1):
  if list[i] == list[i+1]:
    ans = 'POSSIBLE'
    break
print(ans)