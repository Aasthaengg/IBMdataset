import itertools
import numpy as np

n,m,x = map(int, input().split())
A = np.array([[int(x) for x in input().split()] for i in range(n)])
lis, min_ = range(n), 1200001

full = []
#組み合わせの列挙
for r in range(1,n+1):
  comb = list(itertools.combinations(lis,r))
  full.extend(comb)
#print(full)

for i in full:
  #配列の準備
  sum_ = np.zeros(m+1)
  
  #組み合わせの要素合計
  for k in i:
    sum_+=A[k]
    #print(sum_)
    
  #Aが全てx以上もしくは最小コストか否か
  if np.all(sum_[1:]>=x) and min_>sum_[0]:
    min_ = sum_[0]

if min_== 1200001: print('-1')
else: print(int(min_))
