import itertools
 
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
 
# Nが10程度で小さい
# 階乗の全探索をしても間に合う
# Pythonならitertoolsで順列を生成できる！
permutations = list(itertools.permutations([i for i in range(1, N+1)]))
 
a, b = 0, 0
for i, R in enumerate(permutations):
  if R == P: a = i
  if R == Q: b = i

print(abs(a-b))