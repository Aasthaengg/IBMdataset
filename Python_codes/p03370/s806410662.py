[N, X] = list(map(int, input().split()))
list_m = []
for i in range(N):
  list_m.append(int(input()))
X_leftover = X - sum(list_m)
cnt = 0
while X_leftover >= min(list_m):
  X_leftover -= min(list_m)
  cnt += 1
print(len(list_m) + cnt)