n = int(input())
tpred = 1
apred = 1

for i in range(n):
  t, a = map(int, input().split())
  tpred = t*max(-(-tpred//t), -(-apred//a))
  apred = a*max(-(-tpred//t), -(-apred//a))

print(tpred+apred)