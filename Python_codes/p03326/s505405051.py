N, M = map(int, input().split())
scores = [[] for _ in range(8)]

for i in range(N):
  x, y, z = map(int, input().split())
  scores[0].append(x+y+z)
  scores[1].append(x+y-z)
  scores[2].append(x-y+z)
  scores[3].append(-x+y+z)
  scores[4].append(x-y-z)
  scores[5].append(-x+y-z)
  scores[6].append(-x-y+z)
  scores[7].append(-x-y-z)

max_num = -1
for i in range(8):
  tmp = scores[i]
  tmp.sort(reverse=True)
  sum_num = sum(tmp[:M])
  if max_num < sum_num:
    max_num = sum_num

print(max_num)