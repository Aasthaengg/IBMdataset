N,T=map(int,input().split())
route = [tuple(map(int,input().split())) for _ in range(N)]

route = list(filter(lambda x:x[1]<=T,route))
if route==[]:
  print('TLE')
  exit()
route = sorted(route)
print(route[0][0])