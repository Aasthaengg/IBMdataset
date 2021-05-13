N = int(input())
index = {}

for _ in range(N):
  S = input()
  if S not in index: index[S] = 1
  else: index[S] += 1

max_cnt = max(index.values())

ls = [key for key in index.keys() if index[key] == max_cnt]

ls.sort()
for ans in ls:
  print(ans)