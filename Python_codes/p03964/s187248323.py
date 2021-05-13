from math import ceil

N = int(input())
prv_t, prv_a = 1, 1
for _ in range(N):
  t,a = map(int,input().split())
  x = max(-(-prv_t//t), -(-prv_a//a))
  prv_t, prv_a = t*x, a*x
print(prv_t+prv_a)