import itertools

def main():
  n,k = map(int, input().split())
  xy = [tuple(map(int, input().split())) for i in range(n)]
  INF = 10 ** 20
  ans = INF
  for i in itertools.combinations(xy,2):
    max_x,min_x = -INF,INF
    for x,Y in i:
      max_x = max(max_x,x)
      min_x = min(min_x,x)
    for j in itertools.combinations(xy,2):
      max_y,min_y = -INF,INF
      for X,y in j:
        max_y = max(max_y,y)
        min_y = min(min_y,y)
      inrec = 0
      for xi,yi in xy:
        if  (min_x <= xi <= max_x) and (min_y <= yi <= max_y):
          inrec += 1
      if (inrec >= k):
        ans = min(ans,(max_x-min_x)*(max_y-min_y))
  print(ans)
  
if __name__ == '__main__':
  main()