N = int(input())
ls = []
for i in range(N):
  s = input().split()
  ls.append([s[0],-int(s[1]),i+1])
ls.sort()
for i in range(N):
  print(ls[i][2])