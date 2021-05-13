S = input()
N = len(S)
ms = [1]
for i in range(N):
  m = ms[-1]*10%2019
  ms.append(m)
Rs = [0]
for i in range(N):
  c = int(S[N-i-1])
  R = (Rs[-1]+c*ms[i])%2019
  Rs.append(R)
NRs = {}
for R in Rs:
  if R not in NRs:
    NRs[R] = 0
  NRs[R] += 1
r = 0
for R in NRs:
  N = NRs[R]
  r += N*(N-1)//2
print(r)
