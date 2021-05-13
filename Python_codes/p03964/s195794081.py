N = int(input())
T=1
A=1
for i in range(N):
  t,a = map(int,input().split())
  T = max(-(-T//t),-(-A//a))*t
  A = max(-(-T//t),-(-A//a))*a
print(T+A)
