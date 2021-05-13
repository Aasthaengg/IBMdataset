S = str(input())
N = 2 ** (len(S)-1)
l = [] # それぞれの和を格納
for i in range(N):
  m = [S] # 分けた数字を格納
  cnt = 0
  for j in range(len(S)-1):
    if (i >> j) & 1:
      m.append(m[-1][:cnt+1])
      m.append(m[-2][cnt+1:])
      del m[-3]
      cnt = 0
    else:
      cnt += 1
  m = [int(s) for s in m]
  l.append(sum(m))
print(sum(l))