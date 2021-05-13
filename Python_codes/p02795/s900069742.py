h = int(input())
w = int(input())
N = int(input())
cnt, loop = 0, 0
while cnt < N:
  cnt += max(w, h)
  loop += 1
print(loop)