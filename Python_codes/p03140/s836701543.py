n = int(input())
s = [input() for _ in range(3)]
cnt = -n
for i in range(n):
  cnt += len(set([j[i] for j in s]))
print(cnt)