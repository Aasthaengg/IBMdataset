n = int(input())
abc = [list(map(int, input().split())) for _ in range(n)]

aabbcc = [[0], [0], [0]]
tmp = [0]*3
for i in abc:
  for j in range(3):
    tmp[j] = i[j] + max(aabbcc[(j+1)%3][-1], aabbcc[(j+2)%3][-1])
  for j in range(3):
    aabbcc[j].append(tmp[j])
print(max([i[-1] for i in aabbcc]))