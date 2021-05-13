N = int(input())
L = []
for i in range(N):
  a, b = input().split()
  L.append([i+1, a, int(b)])
L.sort(key=lambda List:(List[1], -List[2]))
for l in L:
  print(l[0])