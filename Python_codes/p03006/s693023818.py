import sys
from collections import deque
input = sys.stdin.readline

def main():
  n = int(input())
  ball = [tuple(map(int, input().split())) for i in range(n)]

  ans = n
  for i in range(n):
    for j in range(n):
      p, q = ball[i][0] - ball[j][0], ball[i][1] - ball[j][1]
      par = [-1]*n
      node = [[] for i in range(n)]
      for s in range(n):
        for t in range(n):
          x, y = ball[s][0] - ball[t][0], ball[s][1] - ball[t][1]
          if x == p and y == q:
            node[s].append(t)
            node[t].append(s)
      already = [False]*n
      count = 0
      for k in range(n):
        if already[k]:
          continue
        count += 1
        already[k] = True
        not_yet = deque([k])
        while not_yet:
          key = not_yet.pop()
          for v in node[key]:
            if already[v]:
              continue
            already[v] = True
            not_yet.append(v)
      if ans > count:
        ans = count
  print(ans)

  
main()