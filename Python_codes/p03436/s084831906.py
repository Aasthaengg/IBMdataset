import sys
sys.setrecursionlimit(10000)
H, W = map(int, input().split())
S = []
white = 0
for i in range(H):
  s = str(input())
  S.append(s)
  white += s.count('.')
  
def main(h, w):
  global H
  global W
  global S
  global l
  tmp = []
  if h < H-1:
    if (S[h+1][w]=='.') and ([h+1, w] not in l):
      tmp.append([h+1, w])
  if w < W-1:
    if (S[h][w+1]=='.') and ([h, w+1] not in l):
      tmp.append([h, w+1])
  if 0 < h:
    if (S[h-1][w]=='.') and ([h-1, w] not in l):
      tmp.append([h-1, w])
  if 0 < w:
    if (S[h][w-1]=='.') and ([h, w-1] not in l):
      tmp.append([h, w-1])
  return tmp
    
cnt = 0
l = [[0, 0]]
tmp = [[0, 0]]
for i in range(10000):
  t = []
  for n in tmp:
    u = main(n[0], n[1])
    l += u
    t += u
  if t == []:
    ans = white+1
  elif [H-1, W-1] in t:
    ans = i+2
    break
  else:
    tmp = t
print(white-ans)