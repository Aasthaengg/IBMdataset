n = int(input())
tlst = list(map(int, input().split()))
s = sum(tlst)
m = int(input())
dlst = []
for i in range(m):
  p, x = map(int, input().split())
  print(s - tlst[p - 1] + x)