N = int(input())
sp = [list(input().split()) for i in range(N)]
for i in range(N):
  sp[i].append(i+1)
sorted_data = sorted(sp, key=lambda x:(x[0], -int(x[1])))
for i in range(N):
  print(sorted_data[i][2])