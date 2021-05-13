# -*- coding: utf-8 -*-
import itertools

N, M, Q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(Q)]

# Aの重複組み合わせ結果配列のリスト
A_list = list(itertools.combinations_with_replacement(range(1, M+1), N))
ans = 0
for A in A_list:
  score = 0
  for a, b, c, d in abcd:    
    if A[b-1] - A[a-1] == c:
      score += d
  ans = max(ans, score)
print(ans)