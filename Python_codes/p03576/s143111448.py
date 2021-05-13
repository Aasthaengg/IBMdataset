import sys
input = sys.stdin.readline

def main():
  n, k = map(int, input().split())
  point = [[int(x) for x in input().split()] for _ in range(n)]
  
  ans = pow(10, 18)*4
  for a in range(n):
    for b in range(a+1):
      for c in range(b+1):
        for d in range(c+1):
          x, y = [point[a][0], point[b][0], point[c][0], point[d][0]], [point[a][1], point[b][1], point[c][1], point[d][1]]
          x1, x2, y1, y2 = min(x), max(x), min(y), max(y)
          count = 0
          for e in range(n):
            if x1 <= point[e][0] <= x2 and y1 <= point[e][1] <= y2:
              count += 1
          if count < k:
            continue
          sub = (x2-x1)*(y2-y1)
          if ans > sub:
            ans = sub
  
  print(ans)
  
  
if __name__ == "__main__":
  main()