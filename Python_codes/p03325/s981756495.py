n = int(input())
a = list(map(int, input().split()))
nl = []
for i in range(n):
  bn = bin(a[i])
  nl.append(bn[2:])
count = 0
for i in range(len(nl)):
  lnl = list(nl[i])
  rlnl = lnl[::-1]
  bil = [i for i, x in enumerate(rlnl) if x == '1']
  count += bil[0]
print(count)