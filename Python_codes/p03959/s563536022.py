n = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))

MOD = 10 ** 9 + 7

# T -> の向きでみて増加している場合と初項は対応するAの要素はa >= t
# 同様に、A <- の向きでみて増加している場合と初項は対応するTの要素はa <= t


cap = [min(t, a) for t, a in zip(T, A)]

if max(A) != max(cap) or max(T) != max(cap):
  print(0)
  exit()

capm = max(cap)

cm = cap.count(capm)

ans = 1

if cm > 2:
  for _ in range(cm - 2):
    ans *= capm
    ans %= MOD

for i in range(1, n - 1):
  if cap[i] == capm:
    break
  if cap[i - 1] == cap[i] and cap[i] <= cap[i + 1]:
    if cap[i] < cap[i + 1] or not cap[i + 1] == capm: 
      ans *= cap[i]
      ans %= MOD

for i in reversed(range(1, n - 1)):
  if cap[i] == capm:
    break
  if cap[i + 1] == cap[i] and cap[i] <= cap[i - 1]:
    if cap[i] < cap[i - 1] or not cap[i - 1] == capm: 
      ans *= cap[i]
      ans %= MOD
      
print(ans)