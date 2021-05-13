A, B, C, D = map(int, input().split())
# 体力0以下になる攻撃回数
# 高橋
tcnt = C // B
if C % B != 0:
  tcnt += 1
acnt = A // D
if A % D != 0:
  acnt += 1
# print(tcnt, acnt)
if tcnt <= acnt:
  print('Yes')
else:
  print('No')
