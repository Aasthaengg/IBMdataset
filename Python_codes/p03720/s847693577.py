m,n = map(int, input().split())
road_dict = {k+1:0 for k in range(m)}
for _ in range(n):
  i, j = map(int, input().split())
  road_dict[i] += 1
  road_dict[j] += 1
for v in road_dict.values():
  print(v)