n,m,q=map(int,input().split())
abcd=[list(map(int,input().split())) for i in range(q)]

from itertools import combinations_with_replacement as comb_rplc
cmb = comb_rplc(range(1,m+1),n)
result = 0
for A in cmb:
  tmp = 0
  for a,b,c,d in abcd:
    if A[b-1] - A[a-1] == c:
      tmp += d
  result = max(tmp, result)
print(result)