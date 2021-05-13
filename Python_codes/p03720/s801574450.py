N, M = map(int,input().split())
city = [0]*N
for _ in range(M):
  a_i, b_i = map(int,input().split())
  city[a_i-1]+=1
  city[b_i-1]+=1
for i in range(N):
  print(city[i])