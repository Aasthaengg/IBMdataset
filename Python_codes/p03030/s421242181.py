N = int(input())
D = [list(map(str,input().split())) for _ in range(N)]
for i in range(N):
  D[i].append(i+1)
sorted_d = sorted(D, key = lambda x: (x[0], -int(x[1])))
for i in range(N):
  print(sorted_d[i][2])