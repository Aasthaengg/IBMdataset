import itertools
import math
 
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

# ABC-150-Cの類題
# N!通りの経路を全探索し、各経路の長さを計算し、その平均値を出力する
# 順列組み合わせの生成には、Pythonならitertoolsが使える！
# O(N!N)だが、Nが十分小さいので間に合う
avg = 0
permutations = list(itertools.permutations(range(N)))
for l in permutations:
  for i in range(len(l)-1):
    avg += math.sqrt((xy[l[i+1]][0] - xy[l[i]][0])**2 + (xy[l[i+1]][1] - xy[l[i]][1])**2)

avg /= len(permutations)
print(avg)