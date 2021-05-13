import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
import numpy as np

st = lambda n: bin(n)[2:]
n,k = map(int,readline().split())
a = [int(i) for i in readline().split()]

INF = 10**12
mm = INF.bit_length()
chk = np.array([list(st(i).zfill(mm)) for i in a])

ll = []
q = 0
for num,i in enumerate(chk.T):
  cc = np.count_nonzero(i == '1')
  if cc < n/2:
    q += 2**(mm-1-num)
  ll.append((mm-1-num,2**(mm-1-num)*(n-cc),2**(mm-1-num)*cc))
    
max_V = 0
KK = (k+1).bit_length()
sk = st(k+1).zfill(mm)
sq = st(q).zfill(mm)

for i in range(KK):
  if (k+1)>>i&1 == 1:
    op = q
    if q>>i&1 == 1:
      op -= 2**i
    I = KK-i
    for j in range(mm-KK+I):
      if sq[j] == '1' and sk[j] == '0':
        op -= 2**(mm-1-j)
    V = 0
    for nm,v_1,v_0 in ll:
      if op>>nm & 1 == 1:     
        V += v_1
      else:
        V += v_0
    max_V = max(max_V, V)
    
print(max_V)