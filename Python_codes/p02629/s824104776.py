import math

n = int(input())

'''
(26**(m+1) - 26) / 25 <= n
26**(m+1) <= 25n + 26
m <= log(25n+26, 26) - 1
'''

m = int(math.log(25*n+26, 26) - 1)

d = n - (26**(m+1) - 26) // 25

alphabetTable = ['z']
alphabetTable.extend(chr(i) for i in range(97,123))


if d == 0:
  print('z' * m)

else:
  dd = []
  cnt = 0
  for i in range(1, m+2):
    cnt += 1
    amari = d % 26
    d = d//26 + 1
    if amari == 0:
      d -= 1
    dd.append(amari)
    if d <= 0:
      break
  


  alpha = [alphabetTable[dd[i]] for i in range(cnt)]
  alpha.extend(['a' * (m+1-cnt)])
  alpha.reverse()
  print(''.join(alpha))
