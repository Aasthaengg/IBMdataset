N = int(input())
A = list(map(int, input().split()))

Amean = sum(A)/len(A)
res = 0
minFrameDist = 100
index = 0
for (i, a) in enumerate(A):
  frameDist = abs(Amean-a)
  if frameDist < minFrameDist:
    res = i
    minFrameDist = frameDist

print(res)