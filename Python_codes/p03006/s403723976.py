N = int(input())
XYs = [list(map(int, input().split())) for _ in range(N)]

dic = {}
tmp = 0

for i in range(N):
  for j in range(N):
    if i == j:
      continue
    p = XYs[j][0] - XYs[i][0]
    q = XYs[j][1] - XYs[i][1]

    if "{}_{}".format(p,q) not in dic:
      dic["{}_{}".format(p,q)] = 1
    else:
      dic["{}_{}".format(p,q)] += 1
      
for k in dic:
  if tmp < dic[k]:
    tmp = dic[k]

print(N-tmp)