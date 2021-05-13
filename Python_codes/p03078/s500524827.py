import sys
import itertools
readline = sys.stdin.buffer.readline

X, Y, Z, K = map(int, readline().split())
A = list(map(int, readline().split()))
B = list(map(int, readline().split()))
C = list(map(int, readline().split()))
AB = [a+b for (a,b) in list(itertools.product(A,B))]
AB.sort(reverse=True)
ans = [ab + c for (ab,c) in list(itertools.product(AB[:K],C))]
ans.sort(reverse=True)
for i in range(K):
  print(ans[i])