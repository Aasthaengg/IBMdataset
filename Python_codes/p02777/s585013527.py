w = list(input().split())
n = list(map(int, input().split()))
u = input()

if u == w[0]:
  print(n[0]-1,n[1])
else:
  print(n[0],n[1]-1)