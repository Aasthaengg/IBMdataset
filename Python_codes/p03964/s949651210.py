N = int(input())
TA = [list(map(int,input().split())) for _ in range(N)]
t = 1
a = 1
for i in range(N):
  x = max(-(-t // TA[i][0]),-(-a // TA[i][1]))
  t = TA[i][0] * x
  a = TA[i][1] * x
print(t + a)