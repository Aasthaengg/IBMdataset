from copy import copy
class imos1d:
  def __init__(self, src):
    self.d = [0]
    self.d += copy(src)
    for i in range(len(src)):
      self.d[i+1] += self.d[i]
  
  def query(self, l, r):
    return self.d[r] - self.d[l]
  
N = int(input())
S = input()
B = [ 1 if s == '#' else 0 for s in S ]
W = [ 0 if B[i] else 1 for i in range(len(B)) ]
Bi = imos1d(B)
Wi = imos1d(W)
# print(Bi.d)
# print(Wi.d)
ans = N
for i in range(0, N+1):
  ans = min(ans,
            N - Wi.query(0, i)- Bi.query(i, N))
  # print(N - Wi.query(0, i)- Bi.query(i, N))
print(ans)