def main():  
  N, Y = map(int,input().split())
  Cash = [10000, 5000, 1000]
  for x in range(N+1):
    for y in range(N+1):
      Rem = Y - (10000*x + 5000*y)
      Rem = Rem//1000
      if Rem == (N - x - y) and Rem >=0:
        print(x, y, Rem)
        return 
  print(-1, -1, -1)
  return

main()