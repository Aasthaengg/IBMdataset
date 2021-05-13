n=int(input())
city=min([int(input()) for _ in range(5)])
if n%city==0:
  print(5+n//city-1)
else:
  print(5+n//city)