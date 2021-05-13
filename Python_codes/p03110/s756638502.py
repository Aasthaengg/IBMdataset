def main():
  n = int(input())
  xy = [map(str, input().split()) for _ in range(n)]
  x, u = [list(i) for i in zip(*xy)]
  sum=0
  for i in range(0,n):
    if u[i]=='JPY':
      sum+=float(x[i])
    else:
      sum+=float(x[i])*380000
  print(sum)
  
main()