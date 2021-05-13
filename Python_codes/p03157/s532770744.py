import sys
from collections import deque
input = sys.stdin.readline

def main():
  h, w = map(int, input().split())
  s = [input() for _ in range(h)]
  
  ans = 0
  already = [[False]*w for _ in range(h)]
  for i in range(h):
    for j in range(w):
      if already[i][j] or s[i][j] == ".":
        continue
      already[i][j] = True
      black, white = 0, 0
      not_yet = deque([(i, j)])
      while not_yet:
        p, q = not_yet.pop()
        if s[p][q] == "#":
          black += 1
        else:
          white += 1
        if p > 0 and s[p-1][q] != s[p][q] and not already[p-1][q]:
          not_yet.append((p-1, q))
          already[p-1][q] = True
        if p < h-1 and s[p+1][q] != s[p][q] and not already[p+1][q]:
          not_yet.append((p+1, q))
          already[p+1][q] = True
        if q > 0 and s[p][q-1] != s[p][q] and not already[p][q-1]:
          not_yet.append((p, q-1))
          already[p][q-1] = True
        if q < w-1 and s[p][q+1] != s[p][q] and not already[p][q+1]:
          not_yet.append((p, q+1))
          already[p][q+1] = True
      ans += black*white
  
  print(ans)

  
if __name__ == "__main__":
  main()