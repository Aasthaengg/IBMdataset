n = int(input())
r = [input().split() + [i] for i in range(n)]
for i in range(n):
  r[i][1] = int(r[i][1])
r.sort(reverse=True, key=lambda x:x[1])
r.sort(key=lambda x:x[0])
for i in r:
  print(i[2]+1)