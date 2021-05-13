import sys
input = sys.stdin.readline

H, W, N = map(int, input().split())
ab = set(tuple(map(int, input().split())) for i in range(N))

dxy = {0:[0, 1, 2], 1:[-1, 0, 1], 2:[-2, -1, 0]}
num_all = (H - 2) * (W - 2)
num = [0] * 10
for a, b in ab:
  for i in range(3):
    Da = dxy[i]
    for j in range(3):
      n = 0
      flag = False
      Db = dxy[j]
      for da in Da:
        aa = a + da
        for db in Db:
          bb = b + db
          if aa < 1 or H < aa or bb < 1 or W < bb:
            flag = True
            break
          if (aa, bb) in ab:
            n += 1
        if flag:
          break
      if flag:
        continue
      num[n] += 1

for i in range(2, 10):
  num[i] //= i

num[0] = num_all - sum(num[1:])
print(*num, sep='\n')