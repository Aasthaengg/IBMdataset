A,B,C,K = map(int,input().split())

S = A+B+C
d = A-B

if d > pow(10,18):
  print("unfair")
  exit()
if K%2 == 0:
  print(d)
else:
  print(-d)