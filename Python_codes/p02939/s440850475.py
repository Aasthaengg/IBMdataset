S = str(input())
K = 0
last,now = '',''
for i in range(len(S)):
  now += S[i]
  if i > 0 and now == last:
    continue
  else:
    K += 1
    last = now
    now = ''

print(K)